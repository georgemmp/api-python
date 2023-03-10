from flask_restful import Resource, reqparse
from application.use_cases.get_hotel_use_cases import get_hotels, get_hotel_by_id
from application.use_cases.create_hotel_use_case import create_hotel
from application.use_cases.update_hotel_use_case import update_hotel
from domain.entities.hotel import Hotel
from infrastructure.api.dto.hotel_dto import HotelDTO

class HotelController(Resource):
    def get(self) -> list:
        return get_hotels()
    
    def post(self) -> Hotel:
        dto = HotelDTO.create_dto()
        hotel = Hotel.ommit_id(**dto)
        return create_hotel(hotel), 201
        
        
class HotelControllerId(Resource):
    def get(self, hotel_id: int) -> Hotel:
        return get_hotel_by_id(hotel_id)
    
    def patch(self, hotel_id: int) -> Hotel:
        dto = HotelDTO.create_dto()
        hotel = Hotel.ommit_id(**dto)
        return update_hotel(hotel_id, hotel)