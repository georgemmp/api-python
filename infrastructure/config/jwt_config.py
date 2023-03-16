from flask import jsonify
from flask_jwt_extended import JWTManager
from shared.blacklist import BLACKLIST

def jwt_config(app):
    jwt = JWTManager(app)
    
    @jwt.token_in_blocklist_loader
    def check_blacklist(self, token):
        return token['jti'] in BLACKLIST

    @jwt.revoked_token_loader
    def invalid_token_access(_jwt_header, jwt_data):
        return jsonify({'message': 'Invalid token'}), 401
        

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return identity