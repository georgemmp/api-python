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
    
class HotelFilterDTO:
    
    args = reqparse.RequestParser()
    args.add_argument('cidade', type=str, location="args")
    args.add_argument('estrelas_min', type=float, location="args")
    args.add_argument('estrelas_max', type=float, location="args")
    args.add_argument('diaria_min', type=float, location="args")
    args.add_argument('diaria_max', type=float, location="args")
    args.add_argument('limit', type=int, location="args")
    args.add_argument('offset', type=int, location="args")
    
    def __init__(self, cidade, estrelas_min, estrelas_max, diaria_min, diaria_max, limit, offset) -> None:
        self.cidade = cidade
        self.estrelas_min = estrelas_min,
        self.estrelas_max = estrelas_max,
        self.diaria_min = diaria_min,
        self.diaria_max = diaria_max,
        self.limit = limit,
        self.offset = offset
        
    @classmethod
    def create_dto(cls):
        data = cls.args.parse_args()
        return {key: data[key] for key in data if data[key] is not None}