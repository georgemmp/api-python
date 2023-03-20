from flask import abort
from sqlalchemy import and_
from domain.entities.hotel import Hotel

def __create_query(filters: dict) -> list:
    query = Hotel.query
    filter = __create_filters(filters)
    
    for key in filters.keys():
        query = query.filter(filter[key])
    
    return Hotel.serialize_list(query.all())

def __create_filters(filters: dict):
    return {
        'cidade': Hotel.cidade.like(filters.get('cidade')) if filters.get('cidade') else None,
        'estrelas_min': Hotel.estrelas >= filters.get('estrelas_min') if filters.get('estrelas_min') else None,
        'estrelas_max': Hotel.estrelas <= filters.get('estrelas_max') if filters.get('estrelas_max') else None,
        'diaria_min': Hotel.diaria >= filters.get('diaria_min') if filters.get('diaria_min') else None,
        'diaria_max': Hotel.diaria <= filters.get('diaria_max') if filters.get('diaria_max') else None
    }

def get_hotels(filters: dict) -> list:
    if not filters:
        hotels = Hotel.query.all()
        return Hotel.serialize_list(hotels)
    else:
        return __create_query(filters)

def get_hotel_by_id(hotel_id: int) -> Hotel:
    hotel = Hotel.query.filter_by(hotel_id=hotel_id).first()
    
    if (hotel is None):
       abort (404, 'Hotel {} not found'.format(hotel_id))
    
    return hotel.serialize()