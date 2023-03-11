import bcrypt
from flask import abort
from flask_jwt_extended import create_access_token
from domain.entities.user import User

def login(model: User) -> any:
    user = User.query.filter_by(login=model.login).first()
    
    if user is None:
        abort(401, 'User or password not match')
        
    is_password = bcrypt.checkpw(model.password.encode('utf-8'), user.password.encode('utf-8'))
    
    if is_password is False:
        abort(401, 'User or password not match')
        
    token = create_access_token(identity=user.user_id)
        
    return {'token': token}
        
    