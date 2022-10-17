from src.core.auth.user import User
from src.core.database import db

def list_user():
    return User.query.all() #obtengo la lista de usuarios

def create_user(**kwargs): #obtengo todos los valores 
    user = User(**kwargs)
    db.session.add(user)
    db.session.commit()

    return user