#modelo de issues --> logica de negocio, info de issues
from datetime import datetime
from src.core.database import db

#tabla intermedia
issue_labels = db.Table (
    "issue_labels",
    db.Column("issue_id", db.Integer, db.ForeignKey("issues.id"), primary_key=True),
    db.Column("label_id", db.Integer, db.ForeignKey("labels.id"), primary_key=True),
)

class Issue(db.Model): #heredo de db.Model de flask SQLAlchemist
    
    __tablename__ = "issues"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(50))
    title = db.Column(db.String(100))
    description = db.Column(db.String(225))
    status = db.Column (db.String(50))
    #relacion con el usuario que va a atender determinado issue
    user_id = db.Column (db.Integer, db.ForeignKey("users.id"))
    #le indico que quiero una columna de tipo integer y que es clave foranea de la tabala users.id
    user = db.relationship("User", back_populates="issues")
    #relacion con la tabla intermedia labels
    labels = db.relationship("Label", secondary=issue_labels)
    #metodos para saber cuando fue creada
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now) #cuando se hace un update a este modelo de nuevo ejecuta datetime.now
    inserted_at = db.Column(db.DateTime, default=datetime.now()) #para saber cuando se inserto el ultimo campo 
