from app import create_app, db
from app.models import Produto

app = create_app()

def atualizar_estoque_para_100():
    with app.app_context():
        ids = [1, 2, 3, 4, 5]
        produtos = Produto.query.filter(Produto.id.in_(ids)).all()

        for produto in produtos:
            produto.estoque = 100

        db.session.commit()
        print("Estoque atualizado para 100 para os produtos com IDs 1, 2, 3, 4 e 5.")

if __name__ == '__main__':
    atualizar_estoque_para_100()
