from flask import Flask
from flask_restful import Resource, Api
from resources.hotel import Hotel

app = Flask(__name__)
api = Api(app)

api.add_resource(Hotel, '/hoteis')

if __name__ == '__main__':
    app.run(debug=True, port=8080)