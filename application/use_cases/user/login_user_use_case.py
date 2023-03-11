import bcrypt
from flask import abort, json
from domain.entities.user import User

def login(model: User) -> User:
    user = User.query.filter_by(login=model.login).first()
    
    if user is None:
        abort(403, 'User or password not match')
        
    print(str(user.password))
    print(model.password.encode('utf-8'))
        
    is_password = bcrypt.checkpw(model.password.encode('utf-8'), user.password.encode('utf-8'))
    
    if is_password is False:
        abort(403, 'User or password not match')
        
    return user.serialize()
        
    