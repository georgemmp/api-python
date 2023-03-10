from infrastructure.database.sql_alchemy import database
from domain.utils.serializer import Serializer

class Hotel(database.Model, Serializer):
    
    __tablename__ = 'hotel'
    
    hotel_id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(100))
    estrelas = database.Column(database.Float(precision=1))
    diaria = database.Column(database.Float(precision=2))
    cidade = database.Column(database.String(100))
    
    def __init__(self, nome: str, estrelas: float, diaria: float, cidade: str) -> None:
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade