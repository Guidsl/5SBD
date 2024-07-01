from flask import Blueprint, jsonify, request
from app.services.endereco_services import listar_enderecos, buscar_endereco_por_id, criar_endereco, atualizar_endereco, excluir_endereco

endereco_bp = Blueprint('enderecos', __name__, url_prefix='/enderecos')

@endereco_bp.route('/', methods=['GET'])
def listar_todos_enderecos():
    enderecos = listar_enderecos()
    return jsonify([endereco.to_dict() for endereco in enderecos]), 200

@endereco_bp.route('/<int:endereco_id>', methods=['GET'])
def buscar_endereco(endereco_id):
    endereco = buscar_endereco_por_id(endereco_id)
    if endereco:
        return jsonify(endereco.to_dict()), 200
    else:
        return jsonify({'message': 'Endereço não encontrado'}), 404

@endereco_bp.route('/', methods=['POST'])
def criar_novo_endereco():
    data = request.json
    id_cliente = data.get('id_cliente')
    rua = data.get('rua')
    numero = data.get('numero')
    complemento = data.get('complemento')
    cidade = data.get('cidade')
    estado = data.get('estado')
    cep = data.get('cep')
    pais = data.get('pais')

    novo_endereco = criar_endereco(id_cliente, rua, numero, complemento, cidade, estado, cep, pais)
    return jsonify(novo_endereco.to_dict()), 201

@endereco_bp.route('/<int:endereco_id>', methods=['PUT'])
def atualizar_endereco_existente(endereco_id):
    data = request.json
    rua = data.get('rua')
    numero = data.get('numero')
    complemento = data.get('complemento')
    cidade = data.get('cidade')
    estado = data.get('estado')
    cep = data.get('cep')
    pais = data.get('pais')

    endereco = atualizar_endereco(endereco_id, rua, numero, complemento, cidade, estado, cep, pais)
    if endereco:
        return jsonify(endereco.to_dict()), 200
    else:
        return jsonify({'message': 'Endereço não encontrado'}), 404

@endereco_bp.route('/<int:endereco_id>', methods=['DELETE'])
def excluir_endereco_existente(endereco_id):
    endereco = excluir_endereco(endereco_id)
    if endereco:
        return jsonify(endereco.to_dict()), 200
    else:
        return jsonify({'message': 'Endereço não encontrado'}), 404
