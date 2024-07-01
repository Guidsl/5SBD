from flask import current_app #type: ignore
import requests
from app import db  
from app.models import Cliente, Pedido, ItemPedido, Produto, Endereco  
from datetime import datetime

class ApiConnectService:
    def __init__(self):
        self.api_base_url = 'http://127.0.0.1:5001'  
           
    def get_order(self):
        endpoint = '/orders'
        url = self.api_base_url + endpoint
       
        try:
            response = requests.get(url)
            response.raise_for_status()  
            return response.json()
        except requests.exceptions.RequestException as e:
            current_app.logger.error(f'Failed to connect to API: {e}')
            return {'error': f'Failed to connect to API: {str(e)}'}

    def process_orders_and_store(self):

        orders = self.get_order()
        
        if 'error' in orders:
            return {'error': orders['error']}
        
        for order_data in orders:

            buyer_data = order_data['buyer']
            cliente = Cliente.query.filter_by(cpf=buyer_data['cpf']).first()
            if not cliente:
                cliente = Cliente(nome=buyer_data['name'], email=buyer_data['email'],
                                  cpf=buyer_data['cpf'], telefone=buyer_data.get('phone-number'))
                db.session.add(cliente)

            
            shipping_info = order_data.get('shipping', {}).get('address')
            if shipping_info:
                endereco = Endereco.query.filter_by(id_cliente=cliente.id).first()
                if not endereco:
                    endereco = Endereco(id_cliente=cliente.id,
                                        rua=shipping_info.get('line-1'),
                                        numero=shipping_info.get('line-2'),
                                        complemento=shipping_info.get('line-3'),
                                        cidade=shipping_info.get('city'),
                                        estado=shipping_info.get('state'),
                                        cep=shipping_info.get('postal-code'))
                    db.session.add(endereco)

        
            order_info = order_data['order']
            purchase_date_str = order_info.get('purchase-date')
            payments_date_str = order_info.get('payments-date')

            
            purchase_date = datetime.strptime(purchase_date_str, '%Y-%m-%d').date() if purchase_date_str else None
            payments_date = datetime.strptime(payments_date_str, '%Y-%m-%d').date() if payments_date_str else None
            
            pedido = Pedido(id_cliente=cliente.id, estado='pendente', valor_total=order_info['total-price'],
                            data_criacao=purchase_date, data_pagamento=payments_date)
            db.session.add(pedido)

            
            for product_data in order_data['products']:
                produto = Produto.query.filter_by(nome=product_data['name']).first()
                if produto:
                    item_pedido = ItemPedido(id_pedido=pedido.id, id_produto=produto.id, quantidade=product_data['quantity-purchased'])
                    db.session.add(item_pedido)
            
        db.session.commit()

        return {'message': 'Orders processed and stored successfully'}
