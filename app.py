from flask import Flask
from flask_restful import Api
from infrastructure.api.routes.hotel_routes import create_hotel_routes
from infrastructure.database.sql_alchemy import database
from infrastructure.api.exceptions.error_handler import handle_exception

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hoteis.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_database():
    database.create_all()

create_hotel_routes(api)

if __name__ == '__main__':
    database.init_app(app)
    app.run(debug=True, port=8080)