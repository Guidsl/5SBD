from flask import Blueprint, jsonify, request #type: ignore
from app.services.itemPedido_services import listar_itens_pedido, buscar_item_pedido_por_id, adicionar_item_pedido, atualizar_item_pedido, excluir_item_pedido

item_pedido_bp = Blueprint('itens_pedido', __name__, url_prefix='/itens-pedido')

@item_pedido_bp.route('/', methods=['GET'])
def listar_todos_itens_pedido():
    itens_pedido = listar_itens_pedido()
    return jsonify([item_pedido.to_dict() for item_pedido in itens_pedido]), 200

@item_pedido_bp.route('/<int:item_pedido_id>', methods=['GET'])
def buscar_item_pedido(item_pedido_id):
    item_pedido = buscar_item_pedido_por_id(item_pedido_id)
    if item_pedido:
        return jsonify(item_pedido.to_dict()), 200
    else:
        return jsonify({'message': 'Item de Pedido não encontrado'}), 404

@item_pedido_bp.route('/', methods=['POST'])
def adicionar_novo_item_pedido():
    data = request.json

    novo_item_pedido = adicionar_item_pedido(data)  
    return jsonify(novo_item_pedido.to_dict()), 201

@item_pedido_bp.route('/<int:item_pedido_id>', methods=['PUT'])
def atualizar_item_pedido_existente(item_pedido_id):
    data = request.json
    

    item_pedido = atualizar_item_pedido(item_pedido_id, data) 
    if item_pedido:
        return jsonify(item_pedido.to_dict()), 200
    else:
        return jsonify({'message': 'Item de Pedido não encontrado'}), 404

@item_pedido_bp.route('/<int:item_pedido_id>', methods=['DELETE'])
def excluir_item_pedido_existente(item_pedido_id):
    item_pedido = excluir_item_pedido(item_pedido_id)
    if item_pedido:
        return jsonify(item_pedido.to_dict()), 200
    else:
        return jsonify({'message': 'Item de Pedido não encontrado'}), 404
