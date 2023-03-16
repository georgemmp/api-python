from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt

from infrastructure.api.dto.user_dto import UserDTO
from domain.entities.user import User
from application.use_cases.user.create_user_use_case import create_user
from application.use_cases.user.login_user_use_case import login
from application.use_cases.user.delete_user_use_case import delete_user
from application.use_cases.user.logout_user_use_case import logout

class UserController(Resource):
    
    def post(self) -> User:
        dto = UserDTO.create_dto()
        user = User(**dto)
        
        return create_user(user), 201
    
class UserLoginController(Resource):
    
    def post(self) -> any:
        dto = UserDTO.create_dto()
        user = User(**dto)
        
        return login(user), 200

class UserControllerId(Resource):
    
    @jwt_required()
    def delete(self, user_id: int) -> None:
        return delete_user(user_id), 204
    
class UserLougoutController(Resource):
    
    @jwt_required()
    def post(self):
        return logout(), 200