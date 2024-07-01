from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()


from .cliente import Cliente
from .endereco import Endereco
from .pedido import Pedido
from .itemPedido import ItemPedido
from .produto import Produto
