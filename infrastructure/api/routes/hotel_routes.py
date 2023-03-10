from flask_restful import Api
from infrastructure.api.controllers.hotel_controller import HotelController, HotelControllerId

def create_hotel_routes(api: Api):
    api.add_resource(HotelController, '/hotel/')
    api.add_resource(HotelControllerId, '/hotel/<int:hotel_id>/')
    return api

