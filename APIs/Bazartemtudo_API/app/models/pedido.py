from app import db

class Pedido(db.Model):
    __tablename__ = 'pedidos'

    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    estado = db.Column(db.String(20), nullable=False, default='pendente')   
    valor_total = db.Column(db.Float, nullable=False, default=0.0)   
    data_criacao = db.Column(db.DateTime, nullable=False)
    data_pagamento = db.Column(db.DateTime, nullable=True)
     
    cliente = db.relationship('Cliente', backref=db.backref('pedidos', lazy=True))
    
    def __repr__(self):
        return f'<Pedido {self.id}: Cliente {self.id_cliente}, Estado: {self.estado}, Valor Total: {self.valor_total}>'

    def to_dict(self):
        return {
            'id': self.id,
            'id_cliente': self.id_cliente,
            'estado': self.estado,
            'valor_total': self.valor_total,
            'data_criacao': self.data_criacao,
            'data_pagamento': self.data_pagamento,
            'itens': [{'id_produto': item.id_produto, 'quantidade': item.quantidade} for item in self.itens]

        }
