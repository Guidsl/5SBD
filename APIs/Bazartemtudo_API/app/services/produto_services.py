from app.models.produto import Produto
from app.services.common_services import get_all, get_by_id, add_instance, update_instance, delete_instance
from flask import jsonify #type: ignore
from app import db
def listar_produtos():
    return get_all(Produto)

def buscar_produto_por_id(produto_id):
    return get_by_id(Produto, produto_id)

def criar_produto(nome, descricao, preco):
    novo_produto = Produto(nome=nome, descricao=descricao, preco=preco)
    return add_instance(novo_produto)

def atualizar_produto(produto_id, nome=None, descricao=None, preco=None):  
    produto = buscar_produto_por_id(produto_id)
    if produto:
        if nome:
            produto.nome = nome
        if descricao:
            produto.descricao = descricao
        if preco:
            produto.preco = preco
        update_instance()
    return produto

def excluir_produto(produto_id):
    
    produto = buscar_produto_por_id(produto_id)
    if produto:
        delete_instance(produto)
    return produto

def receber_estoque_produto():
    try:
        
        produtos_para_reestoque = Produto.query.filter_by(tobuy=True).all()

        for produto in produtos_para_reestoque:
            
            produto.estoque += produto.amount_tobuy

            produto.amount_tobuy = 0
            produto.tobuy = False
            
            db.session.add(produto)        
        
        db.session.commit()

        return jsonify({'message': 'Estoque atualizado com sucesso.'})

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    