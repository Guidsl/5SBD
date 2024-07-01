from flask import Flask #type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)

    with app.app_context():
        from .models import cliente, endereco, pedido, itemPedido, produto
        db.create_all()

    from .routes import init_app
    init_app(app)

    return app
