from app import db

class Endereco(db.Model):
    __tablename__ = 'enderecos'

    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    rua = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(20), nullable=False)
    complemento = db.Column(db.String(100), nullable=True)
    cidade = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.String(20), nullable=False)

    
    cliente = db.relationship('Cliente', backref=db.backref('enderecos', lazy=True))

     
    def __repr__(self):
        return f'<Endereco {self.id}: Cliente {self.id_cliente}, {self.rua}, {self.numero}, {self.cidade}, {self.estado}>'

    def to_dict(self):
        return {
            'id': self.id,
            'id_cliente': self.id_cliente,
            'rua': self.rua,
            'numero': self.numero,
            'complemento': self.complemento,
            'cidade': self.cidade,
            'estado': self.estado,
            'cep': self.cep
        } 
    
