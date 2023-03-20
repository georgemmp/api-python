from flask_restful import reqparse

class UserDTO:
    
    args = reqparse.RequestParser()
    args.add_argument('login', type=str, required=True, help= "Loggin field is required")
    args.add_argument('password', type=str, required=True, help="Password field is required")
    
    def __init__(self, login: str, password: str) -> None:
        self.login = login
        self.password = password
        
    @classmethod
    def create_dto(cls):
        return cls.args.parse_args()