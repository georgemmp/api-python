from flask_restful import Api
from .hotel_routes import create_hotel_routes
from .user_routes import create_user_routes
from infrastructure.api.exceptions.error_handler import handle_exception
    
def routes(app):
    api = Api(app, errors=handle_exception)
    
    create_hotel_routes(api)
    create_user_routes(api)