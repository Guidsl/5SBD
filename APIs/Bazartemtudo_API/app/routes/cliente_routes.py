from flask import Blueprint, jsonify, request #type: ignore
from app.services.cliente_services import listar_clientes, buscar_cliente_por_id, criar_cliente, atualizar_cliente, excluir_cliente

cliente_bp = Blueprint('clientes', __name__, url_prefix='/clientes')

@cliente_bp.route('/', methods=['GET'])
def listar_todos_clientes():
    clientes = listar_clientes()
    return jsonify([cliente.to_dict() for cliente in clientes]), 200

@cliente_bp.route('/<int:cliente_id>', methods=['GET'])
def buscar_cliente(cliente_id):
    cliente = buscar_cliente_por_id(cliente_id)
    if cliente:
        return jsonify(cliente.to_dict()), 200
    else:
        return jsonify({'message': 'Cliente não encontrado'}), 404

@cliente_bp.route('/', methods=['POST'])
def criar_novo_cliente():
    data = request.json
    nome = data.get('nome')
    email = data.get('email')
    cpf = data.get('cpf')
    telefone = data.get('telefone')

    novo_cliente = criar_cliente(nome, email, cpf, telefone)
    return jsonify(novo_cliente.to_dict()), 201

@cliente_bp.route('/<int:cliente_id>', methods=['PUT'])
def atualizar_cliente_existente(cliente_id):
    data = request.json
    nome = data.get('nome')
    email = data.get('email')
    cpf = data.get('cpf')
    telefone = data.get('telefone')

    cliente = atualizar_cliente(cliente_id, nome, email, cpf, telefone)
    if cliente:
        return jsonify(cliente.to_dict()), 200
    else:
        return jsonify({'message': 'Cliente não encontrado'}), 404

@cliente_bp.route('/<int:cliente_id>', methods=['DELETE'])
def excluir_cliente_existente(cliente_id):
    cliente = excluir_cliente(cliente_id)
    if cliente:
        return jsonify(cliente.to_dict()), 200
    else:
        return jsonify({'message': 'Cliente não encontrado'}), 404
