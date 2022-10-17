from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app): #recibe la app flask
    db.init_app(app)
    config_db(app)

def config_db(app):
    @app.before_first_request
    def init_database(): #se activa en el primer request que llega a la bd
        db.create_all() #crea todas las tablas 

    @app.teardown_request #se ejecuta cada vez que se termina un request de flask
    def close_session(exception=None): 
        db.session.remove() #ciero la sesion de la bd
    
def reset_db(): #elimina todo lo de la bd, crea todo de nuevo y muestra que termino
    print("Eliminando base de datos...")
    db.drop_all()
    print("Creando base de datos...")
    db.create_all()
    print("Done!")