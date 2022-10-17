#modelo de issues --> logica de negocio, info de issues
from datetime import datetime
from src.core.database import db

class Issue(db.Model): #heredo de db.Model de flask SQLAlchemist
    
    __tablename__ = "issues"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(50))
    title = db.Column(db.String(100))
    description = db.Column(db.String(225))
    status = db.Column (db.String(50))
    #metodos para saber cuando fue creada
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now()) #cuando se hace un update a este modelo de nuevo ejecuta datetime.now
    inserted_at = db.Column(db.DateTime, default=datetime.now()) #para saber cuando se inserto el ultimo campo 
