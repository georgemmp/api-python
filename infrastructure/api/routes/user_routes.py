from flask_restful import Api
from infrastructure.api.controllers.user_controller import UserController

def create_user_routes(api: Api) -> Api:
    api.add_resource(UserController, '/user/')
    return api