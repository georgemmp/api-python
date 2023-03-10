from domain.entities.hotel import Hotel
from infrastructure.database.sql_alchemy import database
from flask import abort

def update_hotel(hotel_id: int, hotel: Hotel) -> Hotel:
    updated_hotel = Hotel.query.filter_by(hotel_id=hotel_id).first()
    
    if updated_hotel is None:
        abort (404, 'Hotel {} not found'.format(hotel_id))
    
    updated_hotel.nome = hotel.nome if hotel.nome is not None else updated_hotel.nome
    updated_hotel.estrelas = hotel.estrelas if hotel.estrelas is not None else updated_hotel.estrelas
    updated_hotel.diaria = hotel.diaria if hotel.diaria is not None else updated_hotel.diaria
    updated_hotel.cidade = hotel.cidade if hotel.cidade is not None else updated_hotel.cidade
    database.session.commit()
    
    return updated_hotel.serialize()