#modelo de user--> logica de negocio, info de usuarios
from datetime import datetime
from src.core.database import db

class User(db.Model): #heredo de db.Model de flask SQLAlchemist
    
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now()) #cuando se hace un update a este modelo de nuevo ejecuta datetime.now
    inserted_at = db.Column(db.DateTime, default=datetime.now()) #para saber cuando se inserto el ultimo campo 
