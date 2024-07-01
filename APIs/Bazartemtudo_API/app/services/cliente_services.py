from app.models.cliente import Cliente
from app.services.common_services import get_all, get_by_id, add_instance, update_instance, delete_instance

def listar_clientes():
    return get_all(Cliente)

def buscar_cliente_por_id(cliente_id):
    return get_by_id(Cliente, cliente_id)

def criar_cliente(nome, email, cpf, telefone):
    novo_cliente = Cliente(nome=nome, email=email, cpf=cpf, telefone=telefone)
    return add_instance(novo_cliente)

def atualizar_cliente(cliente_id, nome=None, email=None, cpf=None, telefone=None):
    cliente = buscar_cliente_por_id(cliente_id)
    if cliente:
        if nome:
            cliente.nome = nome
        if email:
            cliente.email = email
        if cpf:
            cliente.cpf = cpf
        if telefone:
            cliente.telefone = telefone
        update_instance()
    return cliente

def excluir_cliente(cliente_id):
    cliente = buscar_cliente_por_id(cliente_id)
    if cliente:
        delete_instance(cliente)
    return cliente
