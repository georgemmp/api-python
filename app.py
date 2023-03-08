from flask import Flask
from flask_restful import Api
from resources.hotel import Hotel, Hoteis

app = Flask(__name__)
api = Api(app)

api.add_resource(Hoteis, '/hotel/')
api.add_resource(Hotel, '/hotel/<int:hotel_id>/')

if __name__ == '__main__':
    app.run(debug=True, port=8080)