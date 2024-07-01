from flask import Flask, jsonify #type: ignore
from app import create_app
from app.services.apiConnect_services import ApiConnectService
from apscheduler.schedulers.background import BackgroundScheduler #type: ignore
import atexit

app = create_app()
connection = ApiConnectService()

@app.route('/fetch_data', methods=['GET'])
def fetch_data_from_api():
    return connection.process_orders_and_store()

def requisitar_dados_api():
    with app.app_context():
        print("Requisição de dados da API")
        connection.process_orders_and_store()

scheduler = BackgroundScheduler()
scheduler.add_job(func=requisitar_dados_api, trigger="interval", hours=24)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    app.run(debug=True)
