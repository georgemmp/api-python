from flask import json, Flask, Blueprint
from werkzeug.exceptions import HTTPException

# errors = Blueprint('errors', __name__)
app = Flask(__name__)

@app.errorhandler(Exception)
def handle_exception(error):
    response = error.get_response()
    
    response.data = json.dumps({
        "code": error.code,
        "name": error.name,
        "description": error.description,
    })
    
    if isinstance(error, HTTPException):
        response.content_type = "application/json"
        return response
    
    return json.dumps({
        "name": "Internal Server Error",
        "description": "An unexpected error happened",
        "error": str(error)
    }), 500