from domain.entities.hotel import Hotel
from infrastructure.database.sql_alchemy import database
from application.exceptions.application_exceptions import handle_not_found
from flask import json

def get_hotels() -> list:
    return Hotel.query.all()

def get_hotel_by_id(hotel_id: int) -> Hotel:
    hotel = Hotel.query.filter_by(hotel_id=hotel_id).first()
    
    if (hotel is None):
       return handle_not_found('Hotel {} not found'.format(hotel_id))
    
    return hotel