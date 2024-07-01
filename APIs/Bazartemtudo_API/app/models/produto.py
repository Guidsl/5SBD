from app import db

class Produto(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    sku = db.Column(db.String(20), nullable=False)
    upc = db.Column(db.String(20), nullable=False)
    estoque = db.Column(db.Integer, default=0)
    tobuy = db.Column(db.Boolean, default=False)
    amount_tobuy = db.Column(db.Integer, default=0)

    
    def __repr__(self):
        return f'<Produto {self.id}: {self.nome}>'

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'preco': float(self.preco),
            'sku': self.sku,
            'upc': self.upc,
            'estoque': self.estoque,
            'tobuy': self.tobuy,
            'amount_tobuy': self.amount_tobuy
        }
    