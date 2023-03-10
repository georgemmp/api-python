from flask import json, jsonify, Flask
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.errorhandler(Exception)
def handle_exception(error):
    if isinstance(error, HTTPException):
        response = error.get_response()
        
        response.data = json.dumps({
            "code": error.code,
            "name": error.name,
            "description": error.description,
        })
        
        response.content_type = "application/json"
        return response
    
    return jsonify({
            "name": "Internal Server Error",
            "description": "An unexpected error happened",
            "error": str(error)
        }), 500