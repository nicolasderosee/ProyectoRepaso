from flask import Flask
from flask import render_template

from src.web.config import config #me traigo la var config de config.py
from src.web.helpers import handlers
from src.web.controllers.issues import issue_blueprint #importo controller de issues para registrarlo

def create_app(env="development", static_folder="static"): #funcion que crea mi app 
    
    app = Flask(__name__, static_folder=static_folder)

    app.config.from_object(config[env])

    @app.get("/") #decorador, se ejecuta cuando se hace un get al / de mi app 
    def home(): 
        contenido = "mundo"
        return render_template("home.html", contenido=contenido)
    
    #Reigstro controller de issues
    app.register_blueprint(issue_blueprint)

    app.register_error_handler(404, handlers.not_found_error) #cuando encuentre un 404 ejecutar la funcion
    app.register_error_handler(500, handlers.internal_server_error)
    
    return app