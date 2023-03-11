from core.app import app
from infrastructure.database.sql_alchemy import database

@app.before_first_request
def create_database():
    database.create_all()

if __name__ == '__main__':
    database.init_app(app)
    app.run(debug=True, port=8080)