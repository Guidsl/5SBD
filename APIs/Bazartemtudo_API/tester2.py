from app import create_app, db
from app.models import Produto

app = create_app()

# Lista de produtos fictícios
products = [
    {
        "sku": "SKU5830",
        "upc": "590188250965",
        "name": "Banana",
        "currency": "BRL",
        "item-price": 37.46
    },
    {
        "sku": "SKU9759",
        "upc": "744166415371",
        "name": "Cereja",
        "currency": "BRL",
        "item-price": 25.05
    },
    {
        "sku": "SKU8244",
        "upc": "228911296090",
        "name": "Melancia",
        "currency": "BRL",
        "item-price": 85.19
    },
    {
        "sku": "SKU5818",
        "upc": "380261700645",
        "name": "Pera",
        "currency": "BRL",
        "item-price": 31.95
    },
    {
        "sku": "SKU3949",
        "upc": "507214092132",
        "name": "Abacaxi",
        "currency": "BRL",
        "item-price": 61.64
    }
]

def populate_products():
    with app.app_context():
        for product_data in products:
            produto = Produto(
                sku=product_data["sku"],
                upc=product_data["upc"],
                nome=product_data["name"],
                preco=product_data["item-price"]
            )
            db.session.add(produto)
        
        db.session.commit()
        print("Produtos adicionados com sucesso!")

if __name__ == '__main__':
    populate_products()
