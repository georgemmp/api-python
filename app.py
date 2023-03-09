from flask import Flask
from flask_restful import Api
from resources.hotel import Hotel, Hoteis

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hoteis.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_database():
    database.create_all()

api.add_resource(Hoteis, '/hotel/')
api.add_resource(Hotel, '/hotel/<int:hotel_id>/')

if __name__ == '__main__':
    from sql_alchemy import database
    database.init_app(app)
    app.run(debug=True, port=8080)