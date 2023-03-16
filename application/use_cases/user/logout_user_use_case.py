from flask_jwt_extended import get_jwt
from shared.blacklist import BLACKLIST

def logout():
    jwt_id = get_jwt()['jti']
    BLACKLIST.add(jwt_id)
    return {'message': 'Logout success'}
    
    