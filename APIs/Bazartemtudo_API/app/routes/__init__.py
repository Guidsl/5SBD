from flask import Blueprint #type: ignore
from .cliente_routes import cliente_bp
from .endereco_routes import endereco_bp
from .pedido_routes import pedido_bp
from .itemPedido_routes import item_pedido_bp
from .produto_routes import produto_bp
 


def init_app(app):
    app.register_blueprint(cliente_bp)
    app.register_blueprint(endereco_bp)
    app.register_blueprint(pedido_bp)
    app.register_blueprint(item_pedido_bp)
    app.register_blueprint(produto_bp)
    
