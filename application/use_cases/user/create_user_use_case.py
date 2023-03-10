from domain.entities.user import User
from infrastructure.database.sql_alchemy import database

def create_user(user: User) -> User:
    database.session.add(user)
    database.session.commit();
    
    return user.serialize()