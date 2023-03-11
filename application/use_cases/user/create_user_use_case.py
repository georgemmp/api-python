import bcrypt
from domain.entities.user import User
from infrastructure.database.sql_alchemy import database

def create_user(user: User) -> any:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), salt)
    
    user.password = hashed_password.decode('utf-8')
    
    database.session.add(user)
    database.session.commit();
    
    return user.serialize()