from app.models.itemPedido import ItemPedido
from app.services.common_services import get_all, get_by_id, add_instance, update_instance, delete_instance

def listar_itens_pedido():
    return get_all(ItemPedido)

def buscar_item_pedido_por_id(item_pedido_id):
    return get_by_id(ItemPedido, item_pedido_id)

def adicionar_item_pedido(id_pedido, id_produto, quantidade):
    novo_item_pedido = ItemPedido(id_pedido=id_pedido, id_produto=id_produto, quantidade=quantidade)
    return add_instance(novo_item_pedido)

def atualizar_item_pedido(item_pedido_id, quantidade=None):
    item_pedido = buscar_item_pedido_por_id(item_pedido_id)
    if item_pedido:
        if quantidade is not None:
            item_pedido.quantidade = quantidade
        update_instance()
    return item_pedido

def excluir_item_pedido(item_pedido_id):
    item_pedido = buscar_item_pedido_por_id(item_pedido_id)
    if item_pedido:
        delete_instance(item_pedido)
    return item_pedido
