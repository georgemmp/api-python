from flask_restful import Resource
from infrastructure.api.dto.user_dto import UserDTO
from domain.entities.user import User
from application.use_cases.user.create_user_use_case import create_user
from application.use_cases.user.login_user_use_case import login

class UserController(Resource):
    
    def post(self):
        dto = UserDTO.create_dto()
        user = User(**dto)
        
        return create_user(user), 201
    
class UserLoginController(Resource):
    
    def post(self):
        dto = UserDTO.create_dto()
        user = User(**dto)
        
        return login(user), 200
        