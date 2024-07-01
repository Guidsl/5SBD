from app.models.endereco import Endereco
from app.services.common_services import get_all, get_by_id, add_instance, update_instance, delete_instance

def listar_enderecos():
    return get_all(Endereco)

def buscar_endereco_por_id(endereco_id):
    return get_by_id(Endereco, endereco_id)

def criar_endereco(id_cliente, rua, numero, complemento, cidade, estado, cep, pais):
    novo_endereco = Endereco(id_cliente=id_cliente, rua=rua, numero=numero, complemento=complemento,
                             cidade=cidade, estado=estado, cep=cep, pais=pais)
    return add_instance(novo_endereco)

def atualizar_endereco(endereco_id, rua=None, numero=None, complemento=None, cidade=None, estado=None, cep=None, pais=None):
    endereco = buscar_endereco_por_id(endereco_id)
    if endereco:
        if rua:
            endereco.rua = rua
        if numero:
            endereco.numero = numero
        if complemento:
            endereco.complemento = complemento
        if cidade:
            endereco.cidade = cidade
        if estado:
            endereco.estado = estado
        if cep:
            endereco.cep = cep
        if pais:
            endereco.pais = pais
        update_instance()
    return endereco

def excluir_endereco(endereco_id):
    endereco = buscar_endereco_por_id(endereco_id)
    if endereco:
        delete_instance(endereco)
    return endereco
