from flask_restful import Api
from infrastructure.api.controllers.hotel_controller import HotelController, HotelListController

def create_hotel_routes(api: Api):
    api.add_resource(HotelController, '/hotel/<int:hotel_id>/')
    api.add_resource(HotelListController, '/hotel/')
    return api

