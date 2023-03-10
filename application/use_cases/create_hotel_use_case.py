from domain.entities.hotel import Hotel
from infrastructure.database.sql_alchemy import database

def create_hotel(hotel: Hotel):
    database.session.add(hotel)
    database.session.commit()
    
    return hotel.serialize()
    