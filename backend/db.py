from server import db
from server import app

def dbCreation ():
    with app.app_context():
        db.create_all()

dbCreation()