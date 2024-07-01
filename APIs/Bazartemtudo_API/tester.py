from flask import Flask # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from app import create_app, db  
from app.services.apiConnect_services import ApiConnectService  
from app.models import Cliente, Pedido, ItemPedido, Produto  

app = create_app()  
app.app_context().push()  

api_service = ApiConnectService()

def test_process_orders_and_store():
    result = api_service.process_orders_and_store()
    if 'error' in result:
        print(f'Erro ao processar os pedidos: {result["error"]}')
    else:
        print('Pedidos processados e armazenados com sucesso!')

    
    print('\nClientes no banco de dados:')
    clientes = Cliente.query.all()
    for cliente in clientes:
        print(cliente)

    print('\nPedidos no banco de dados:')
    pedidos = Pedido.query.all()
    for pedido in pedidos:
        print(pedido)
        print('Itens do pedido:')
        for item in pedido.itens:
            print(item)

    print('\nProdutos no banco de dados:')
    produtos = Produto.query.all()
    for produto in produtos:
        print(produto)

if __name__ == '__main__':
    test_process_orders_and_store()
