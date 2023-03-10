from flask_restful import reqparse

class HotelDTO:
    args = reqparse.RequestParser()
    args.add_argument('nome')
    args.add_argument('estrelas')
    args.add_argument('diaria')
    args.add_argument('cidade')
    
    def __init__(self, nome: str, estrelas: float, diaria: float, cidade: str) -> None:
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
        
    @classmethod
    def create_dto(cls):
        return cls.args.parse_args()