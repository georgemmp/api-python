from infrastructure.database.sql_alchemy import database
from domain.utils.serializer import Serializer

class User(database.Model, Serializer):
    
    __tablename__ = 'user'
    
    user_id = database.Column(database.Integer, primary_key=True)
    login = database.Column(database.String(50), unique=True)
    password = database.Column(database.String(50))
    
    def __init__(self, login: str, password: str) -> None:
        self.login = login
        self.password = password