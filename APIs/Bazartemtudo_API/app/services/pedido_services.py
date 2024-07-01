from app.models import Pedido, ItemPedido, Produto
from app import db
from app.services.common_services import get_all, get_by_id, add_instance, update_instance, delete_instance
from flask import jsonify #type: ignore
from datetime import datetime
from dateutil.parser import parse

def listar_pedidos():
    return  get_all(Pedido)


def tratar_pedidos_por_valor_total():
    pedidos = Pedido.query.filter_by(estado='pendente').order_by(Pedido.valor_total.desc()).all()
    pedidos_tratados = []
    itens_para_comprar = {}  # Dicionário para armazenar itens que precisam ser comprados
    pedidos_nao_atendidos = []  # Lista para armazenar pedidos não atendidos

    for pedido in pedidos:
        estoque_disponivel = True
        itens_para_atualizar = []

        # Verifica se há estoque suficiente para cada item do pedido
        for item_pedido in pedido.itens:
            produto = Produto.query.get(item_pedido.id_produto)
            if produto:
                if produto.estoque >= item_pedido.quantidade:
                    itens_para_atualizar.append((produto, item_pedido.quantidade))
                else:
                    estoque_disponivel = False
                    if item_pedido.id_produto in itens_para_comprar:
                        itens_para_comprar[item_pedido.id_produto]['quantidade_para_compra'] += item_pedido.quantidade
                    else:
                        itens_para_comprar[item_pedido.id_produto] = {
                            'id_produto': item_pedido.id_produto,
                            'quantidade_para_compra': item_pedido.quantidade,
                            'nome': produto.nome,
                            'upc': produto.upc
                        }
                        # Atualiza a quantidade para comprar (amount_tobuy) no produto
                        produto.amount_tobuy += item_pedido.quantidade
                        
                    pedidos_nao_atendidos.append({
                        'id_pedido': pedido.id,
                        'mensagem': f'Estoque de {produto.nome} insuficiente para atender o pedido {pedido.id}'
                    })

        if estoque_disponivel:
            # Atualiza o estoque e marca o pedido como processado
            for produto, quantidade in itens_para_atualizar:
                produto.estoque -= quantidade
                db.session.add(produto)

            pedido.estado = 'processado'
            db.session.add(pedido)
            pedidos_tratados.append({
                'id': pedido.id,
                'itens': [{'id_produto': item.id_produto, 'nome': item.produto.nome, 'quantidade': item.quantidade} for item in pedido.itens],
                'valor_total': pedido.valor_total,
                'data_criacao': pedido.data_criacao.strftime('%Y-%m-%d %H:%M:%S'),
                'data_pagamento': pedido.data_pagamento.strftime('%Y-%m-%d %H:%M:%S') if pedido.data_pagamento else None
            })

    db.session.commit()
    atualizar_estoque_compras(itens_para_comprar.values())

    return jsonify({
        'message': 'Pedidos processados com sucesso.',
        'pedidos_tratados': pedidos_tratados,
        'itens_para_comprar': list(itens_para_comprar.values()),
        'pedidos_nao_atendidos': pedidos_nao_atendidos
    })


def atualizar_estoque_compras(itens_para_comprar):
    for item_compra in itens_para_comprar:
        produto_id = item_compra['id_produto']
        quantidade_compra = item_compra['quantidade_para_compra']

        produto = Produto.query.get(produto_id)
        if produto:
            produto.tobuy = True
            produto.amount_tobuy = quantidade_compra 
            """ if produto.amount_tobuy:
                produto.amount_tobuy += quantidade_compra
            else:
                produto.amount_tobuy = quantidade_compra """

            db.session.add(produto)
        else:
            print(f'Produto não encontrado com id {produto_id}')

    db.session.commit()

def tratar_pedidos_por_data_pagamento():
    # Busca os pedidos pendentes, ordenados pela data de pagamento em ordem crescente (mais antigos primeiro)
    pedidos = Pedido.query.filter_by(estado='pendente').order_by(Pedido.data_pagamento.asc()).all()
    pedidos_tratados = []
    itens_para_comprar = {}  # Dicionário para armazenar itens que precisam ser comprados
    pedidos_nao_atendidos = []  # Lista para armazenar pedidos não atendidos

    for pedido in pedidos:
        estoque_disponivel = True
        itens_para_atualizar = []

        # Verifica se há estoque suficiente para cada item do pedido
        for item_pedido in pedido.itens:
            produto = Produto.query.get(item_pedido.id_produto)
            if produto and produto.estoque >= item_pedido.quantidade:
                itens_para_atualizar.append((produto, item_pedido.quantidade))
            else:
                # Estoque insuficiente, marca o pedido como não atendido
                estoque_disponivel = False
                if produto:
                    if item_pedido.id_produto in itens_para_comprar:
                        itens_para_comprar[item_pedido.id_produto]['quantidade_para_compra'] += item_pedido.quantidade
                    else:
                        itens_para_comprar[item_pedido.id_produto] = {
                            'id_produto': item_pedido.id_produto,
                            'quantidade_para_compra': item_pedido.quantidade,
                            'nome': produto.nome,
                            'upc': produto.upc  # Adicione aqui o UPC do produto, se existir
                        }
                pedidos_nao_atendidos.append({
                    'id_pedido': pedido.id,
                    'mensagem': f'Estoque insuficiente para atender o pedido {pedido.id}'
                })

        if estoque_disponivel:
            # Atualiza o estoque e marca o pedido como processado
            for produto, quantidade in itens_para_atualizar:
                produto.estoque -= quantidade
            
            pedido.estado = 'processado'
            db.session.add(pedido)
            pedidos_tratados.append({
                'id': pedido.id,
                'itens': [{'id_produto': item.id_produto, 'nome': item.produto.nome, 'quantidade': item.quantidade} for item in pedido.itens],
                'valor_total': pedido.valor_total,
                'data_criacao': pedido.data_criacao.strftime('%Y-%m-%d %H:%M:%S'),
                'data_pagamento': pedido.data_pagamento.strftime('%Y-%m-%d %H:%M:%S') if pedido.data_pagamento else None
            })

    # Confirma as alterações no banco de dados
    db.session.commit()

    # Converte o dicionário para uma lista para o formato JSON
    itens_para_comprar_final = list(itens_para_comprar.values())

    # Função fictícia para atualizar o estoque com as compras necessárias
    atualizar_estoque_compras(itens_para_comprar_final)

    # Retorna a resposta como JSON
    return jsonify({
        'message': 'Pedidos processados com sucesso.',
        'pedidos_tratados': pedidos_tratados,
        'itens_para_comprar': itens_para_comprar_final,
        'pedidos_nao_atendidos': pedidos_nao_atendidos
    })


def buscar_por_data_pagamento():
    # Busca os pedidos pendentes, ordenados pela data de criação em ordem crescente (mais antigos primeiro)
    return Pedido.query.order_by(Pedido.data_criacao.asc()).all()
    
def buscar_pedido_por_id(pedido_id):
    # Retorna um pedido específico pelo ID #
    return get_by_id(Pedido, pedido_id)

def criar_pedido(id_cliente, estado):
    # Cria um novo pedido #
    novo_pedido = Pedido(id_cliente=id_cliente, estado=estado)
    return add_instance(novo_pedido)

def atualizar_pedido(pedido_id, estado=None):
    # Atualiza o estado de um pedido #
    pedido = buscar_pedido_por_id(pedido_id)
    if pedido:
        if estado:
            pedido.estado = estado
        update_instance()
    return pedido

def excluir_pedido(pedido_id):
    # Exclui um pedido #
    pedido = buscar_pedido_por_id(pedido_id)
    if pedido:
        delete_instance(pedido)
    return pedido
