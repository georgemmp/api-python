from flask import abort
from domain.entities.user import User
from infrastructure.database.sql_alchemy import database

def delete_user(user_id: int) -> None:
    user = User.query.filter_by(user_id=user_id).first()
    
    if user is None:
        abort(404, 'User {} not found'.format(user_id))
        
    database.session.delete(user)
    database.session.commit()