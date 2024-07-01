from app import create_app, db
from app.models.cliente import Cliente
from app.models.endereco import Endereco
from app.models.pedido import Pedido
from app.models.itemPedido import ItemPedido
from app.models.produto import Produto


app = create_app()

with app.app_context():
    # Criação de clientes
    cliente1 = Cliente(nome='João', email='joao@example.com', cpf='123.456.789-00', telefone='(11) 9999-8888')
    cliente2 = Cliente(nome='Maria', email='maria@example.com', cpf='987.654.321-00', telefone='(11) 7777-6666')

    # Criação de endereços
    # Exemplo de criação de objeto Endereco corrigido
    endereco1 = Endereco(rua='Rua A', numero='123', cidade='São Paulo', estado='SP', cep='01000-000', cliente=cliente1)
    endereco2 = Endereco(rua='Rua B', numero='456', cidade='Rio de Janeiro', estado='RJ', cep='20000-000', cliente=cliente2)	

    # Criação de produtos
    produto1 = Produto(nome='Camiseta', descricao='Camiseta branca', preco=29.99, estoque=100)
    produto2 = Produto(nome='Calça', descricao='Calça jeans', preco=79.99, estoque=50)

    # Criação de pedidos
    pedido1 = Pedido(cliente=cliente1)
    pedido2 = Pedido(cliente=cliente2)

    # Criação de itens de pedido
    item_pedido1 = ItemPedido(pedido=pedido1, produto=produto1, quantidade=2)
    item_pedido2 = ItemPedido(pedido=pedido2, produto=produto2, quantidade=1)

    # Adicionando objetos ao banco de dados
    db.session.add(cliente1)
    db.session.add(cliente2)
    db.session.add(endereco1)
    db.session.add(endereco2)
    db.session.add(produto1)
    db.session.add(produto2)
    db.session.add(pedido1)
    db.session.add(pedido2)
    db.session.add(item_pedido1)
    db.session.add(item_pedido2)

    # Commit para salvar as alterações no banco de dados
    db.session.commit()

    print("Dados populados com sucesso!")
