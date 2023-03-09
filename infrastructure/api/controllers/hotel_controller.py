from flask_restful import Resource, reqparse
from application.use_cases.get_hotel_use_cases import get_hotels, get_hotel_by_id
from domain.entities.hotel import Hotel

class HotelListController(Resource):
    def get(self) -> list:
        return get_hotels()
        
class HotelController(Resource):
    def get(self, hotel_id: str) -> Hotel:
        return get_hotel_by_id(hotel_id)