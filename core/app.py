from flask import Flask
from flask_jwt_extended import JWTManager

from infrastructure.api.exceptions.error_handler import handle_exception
from infrastructure.config.db_config import sqlite_db
from infrastructure.api.routes.api_routes import routes

app = Flask(__name__)
app.register_error_handler(Exception, handle_exception)
app.config['SQLALCHEMY_DATABASE_URI'] = sqlite_db['database']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'OSegredoAgoraEOutro'

jwt = JWTManager(app)

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return identity

routes(app)

