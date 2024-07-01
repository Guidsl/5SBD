from flask import Blueprint, jsonify, request #type: ignore
from app.services.produto_services import listar_produtos, buscar_produto_por_id, criar_produto, atualizar_produto, excluir_produto, receber_estoque_produto

produto_bp = Blueprint('produtos', __name__, url_prefix='/produtos')

@produto_bp.route('/', methods=['GET'])
def listar_todos_produtos():
    produtos = listar_produtos()
    return jsonify([produto.to_dict() for produto in produtos]), 200

@produto_bp.route('/<int:produto_id>', methods=['GET'])
def buscar_produto(produto_id):
    produto = buscar_produto_por_id(produto_id)
    if produto:
        return jsonify(produto.to_dict()), 200
    else:
        return jsonify({'message': 'Produto não encontrado'}), 404

@produto_bp.route('/', methods=['POST'])
def criar_novo_produto():
    data = request.json
     

    novo_produto = criar_produto(data)   
    return jsonify(novo_produto.to_dict()), 201

@produto_bp.route('/recebendo_estoque', methods=['POST'])
def receber_estoque():
    return receber_estoque_produto()


@produto_bp.route('/<int:produto_id>', methods=['PUT'])
def atualizar_produto_existente(produto_id):
    data = request.json
     

    produto = atualizar_produto(produto_id, data)   
    if produto:
        return jsonify(produto.to_dict()), 200
    else:
        return jsonify({'message': 'Produto não encontrado'}), 404

@produto_bp.route('/<int:produto_id>', methods=['DELETE'])
def excluir_produto_existente(produto_id):
    produto = excluir_produto(produto_id)
    if produto:
        return jsonify(produto.to_dict()), 200
    else:
        return jsonify({'message': 'Produto não encontrado'}), 404
