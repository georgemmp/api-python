from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

hoteis = [
    {
        'hote_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
    },
    {
        'hote_id': 'beta',
        'nome': 'Beta Hotel',
        'estrelas': 4.5,
        'diaria': 420.34,
        'cidade': 'Belo Horizonte'
    },
    {
        'hote_id': 'gama',
        'nome': 'Gama Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Florianópolis'
    }
]

class Hotel(Resource):
    def get(self):
        return {'hoteis': hoteis}
    
api.add_resource(Hotel, '/hoteis')

if __name__ == '__main__':
    app.run(debug=True, port=8080)