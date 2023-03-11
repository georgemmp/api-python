from flask import Flask
from infrastructure.api.exceptions.error_handler import handle_exception
from infrastructure.config.db_config import sqlite_db
from infrastructure.api.routes.api_routes import routes

app = Flask(__name__)
app.register_error_handler(Exception, handle_exception)
app.config['SQLALCHEMY_DATABASE_URI'] = sqlite_db['database']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'OSegredoAgoraEOutro'

routes(app)