from flask import abort
from domain.entities.hotel import Hotel
from infrastructure.database.sql_alchemy import database

def delete_hotel(hotel_id: int) -> None:
    hotel = Hotel.query.filter_by(hotel_id=hotel_id).first()
    
    if (hotel is None):
        abort(404, 'Hotel {} not found'.format(hotel_id))
    
    database.session.delete(hotel)
    database.session.commit()
    