from flask import Blueprint, jsonify #type: ignore
from app.services.pedido_services import listar_pedidos, tratar_pedidos_por_valor_total, buscar_pedido_por_id, buscar_por_data_pagamento, tratar_pedidos_por_data_pagamento

pedido_bp = Blueprint('pedidos', __name__, url_prefix='/pedidos')


@pedido_bp.route('/', methods=['GET'])
def listar_todos_pedidos():
    pedidos = listar_pedidos()
    return jsonify([pedido.to_dict() for pedido in pedidos]), 200

@pedido_bp.route('/datas', methods=['GET'])
def listar_todos_pedidos_por_data():
    pedidos = buscar_por_data_pagamento()
    return jsonify([pedido.to_dict() for pedido in pedidos]), 200


@pedido_bp.route('/tratar', methods=['GET'])
def pedidos_para_tratar():
    return tratar_pedidos_por_valor_total()

@pedido_bp.route('/tratamento_com_estoque', methods=['GET'])
def tratamento_com_estoque():
    return tratar_pedidos_por_data_pagamento()

@pedido_bp.route('/<int:pedido_id>', methods=['GET'])
def buscar_pedido(pedido_id):
    pedido = buscar_pedido_por_id(pedido_id)
    if pedido:
        return jsonify(pedido.to_dict()), 200
    else:
        return jsonify({'message': 'Pedido não encontrado'}), 404