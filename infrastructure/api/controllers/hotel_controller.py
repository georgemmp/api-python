from flask_restful import Resource
from application.use_cases.hotel.get_hotel_use_cases import get_hotels, get_hotel_by_id
from application.use_cases.hotel.create_hotel_use_case import create_hotel
from application.use_cases.hotel.update_hotel_use_case import update_hotel
from application.use_cases.hotel.delete_hotel_use_case import delete_hotel
from domain.entities.hotel import Hotel
from ..dto.hotel_dto import HotelDTO
from ..dto.hotel_dto import HotelFilterDTO

class HotelController(Resource):
    def get(self) -> list:
        filters = HotelFilterDTO.create_dto()
        
        return get_hotels(filters), 200
    
    def post(self) -> Hotel:
        dto = HotelDTO.create_dto()
        hotel = Hotel(**dto)
        return create_hotel(hotel), 201
        
        
class HotelControllerId(Resource):
    def get(self, hotel_id: int) -> Hotel:
        return get_hotel_by_id(hotel_id), 200
    
    def patch(self, hotel_id: int) -> Hotel:
        dto = HotelDTO.create_dto()
        hotel = Hotel(**dto)
        return update_hotel(hotel_id, hotel), 200
    
    def delete(self, hotel_id: int) -> None:
        return delete_hotel(hotel_id), 204