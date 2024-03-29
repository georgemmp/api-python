from flask_restful import Api
from ..controllers.user_controller import UserController, UserLoginController, UserControllerId, UserLougoutController

def create_user_routes(api: Api) -> Api:
    api.add_resource(UserController, '/user/')
    api.add_resource(UserControllerId, '/user/<int:user_id>/')
    api.add_resource(UserLoginController, '/login/')
    api.add_resource(UserLougoutController, '/logout/')
    return api