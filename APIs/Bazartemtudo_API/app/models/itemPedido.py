from app import db

class ItemPedido(db.Model):
    __tablename__ = 'itens_pedidos'

    id = db.Column(db.Integer, primary_key=True)
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)
    id_produto = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)

     
    pedido = db.relationship('Pedido', backref=db.backref('itens', lazy=True))
    produto = db.relationship('Produto', backref=db.backref('itens_pedidos', lazy=True))

     
    def __repr__(self):
        return f'<ItemPedido {self.id}: Pedido {self.id_pedido}, Produto {self.id_produto}, Quantidade: {self.quantidade}>'

    def to_dict(self):
        return {
            'id': self.id,
            'id_pedido': self.id_pedido,
            'id_produto': self.id_produto,
            'quantidade': self.quantidade
        }
    