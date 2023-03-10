from domain.entities.hotel import Hotel
from flask import abort

def get_hotels() -> list:
    hotels = Hotel.query.all()
    return Hotel.serialize_list(hotels)

def get_hotel_by_id(hotel_id: int) -> Hotel:
    hotel = Hotel.query.filter_by(hotel_id=hotel_id).first()
    
    if (hotel is None):
       abort (404, 'Hotel {} not found'.format(hotel_id))
    
    return hotel.serialize()