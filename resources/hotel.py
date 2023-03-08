from flask_restful import Resource, reqparse

hoteis = [
    {
        'hotel_id': 1,
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
    },
    {
        'hotel_id': 2,
        'nome': 'Beta Hotel',
        'estrelas': 4.5,
        'diaria': 420.34,
        'cidade': 'Belo Horizonte'
    },
    {
        'hotel_id': 3,
        'nome': 'Gama Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Florianópolis'
    }
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
        
    def find_hotel_by_id(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None
            
    def get(self, hotel_id):
        hotel = self.find_hotel_by_id(hotel_id)
        
        if hotel is None:
            return {'message': 'Not found'}, 404
        return hotel   
        
    def post(self, hotel_id):
        hotel = self.find_hotel_by_id(hotel_id)
        
        if hotel:
            return { 'message': 'Hotel id already exists' }, 400
        
        dados = Hotel.argumentos.parse_args()
        
        novo_hotel = {
            'hotel_id': hotel_id,
            **dados
        }
        
        hoteis.append(novo_hotel)
        return novo_hotel
    
    def patch(self, hotel_id):
        hotel = self.find_hotel_by_id(hotel_id)
        
        if hotel is None:
            return {'message': 'Not found'}, 404
        
        dados = Hotel.argumentos.parse_args()
        
        novo_hotel = {
            'hotel_id': hotel_id,
            **dados
        }
        
        hotel.update(novo_hotel)
        
        return hotel
    
    def delete(self, hotel_id):
        hotel = self.find_hotel_by_id(hotel_id)
        print(hotel)
        if hotel is None:
            return {'message': 'Not found'}, 404
        
        index = next((index for (index, hotel) in enumerate(hoteis) if hotel['hotel_id'] == hotel_id), None)
        hotel = hoteis[index]
        hoteis.remove(hotel)
        return {'message': 'Hotel {} was deleted'.format(hotel_id)}, 200
        