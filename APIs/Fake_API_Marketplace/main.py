from flask import Flask, jsonify, request #type: ignore
from faker import Faker
import random

app = Flask(__name__)
faker = Faker()

def generate_random_order(num_products=faker.random_int(min=1, max=3)):
    products = [
            
                {
                    "sku": "SKU5830",
                    "upc": "590188250965",
                    "name": "Banana",
                    "quantity-purchased": random.randint(1, 10),
                    "currency": "BRL",
                    "item-price": 37.46
                },
                {
                    "sku": "SKU9759",
                    "upc": "744166415371",
                    "name": "Cereja",
                    "quantity-purchased": random.randint(1, 10),
                    "currency": "BRL",
                    "item-price": 25.05
                },
                {
                    "sku": "SKU8244",
                    "upc": "228911296090",
                    "name": "Melancia",
                    "quantity-purchased": random.randint(1, 10),
                    "currency": "BRL",
                    "item-price": 85.19
                },
                {
                    "sku": "SKU5818",
                    "upc": "380261700645",
                    "name": "Pera",
                    "quantity-purchased": random.randint(1, 10),
                    "currency": "BRL",
                    "item-price": 31.95
                },
                {
                    "sku": "SKU3949",
                    "upc": "507214092132",
                    "name": "Abacaxi",
                    "quantity-purchased": random.randint(1, 10),
                    "currency": "BRL",
                    "item-price": 61.64
                }
            ]
        

    total_price = sum(product['item-price'] * product['quantity-purchased'] for product in products)
    produtos_in = random.sample(products, num_products)
    order_data = {
        "order": {
            "order-id": f"ORD{random.randint(100000000, 999999999)}",
            "order-item-id": f"ITEM{random.randint(100000000, 999999999)}",
            "purchase-date": faker.date_this_year().strftime('%Y-%m-%d'),
            "payments-date": faker.date_this_year().strftime('%Y-%m-%d'),
            "total-price": round(total_price, 2)
        },
        "buyer": {
            "email": faker.email(),
            "name": faker.name(),
            "cpf": faker.ssn(),
            "phone-number": faker.phone_number()
        },
        "products": produtos_in,
        "shipping": {
            "service-level": random.choice(["standard", "express", "overnight"]),
            "address": {
                "line-1": faker.street_address(),
                "line-2": faker.secondary_address(),
                "line-3": "",
                "city": faker.city(),
                "state": faker.state_abbr(),
                "postal-code": faker.zipcode(),
                "country": faker.country_code()
            }
        }
    }
    
    return order_data

@app.route('/orders', methods=['GET'])
def get_orders():
    num_orders = int(request.args.get('num_orders', 5))  
    orders = [generate_random_order() for _ in range(num_orders)]
    return jsonify(orders), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
