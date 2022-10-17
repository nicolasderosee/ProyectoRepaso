from flask import Flask
from flask import render_template

from src.core import database
from src.core import seeds
from src.web.config import config 
from src.web.helpers import handlers
from src.web.controllers.issues import issue_blueprint #importo controller de issues para registrarlo

def create_app(env="development", static_folder="static"): #funcion que crea mi app 
    app = Flask(__name__, static_folder=static_folder)

    app.config.from_object(config[env])

    database.init_app(app) #ejecuto el metodo init_app y le mando mi app flask


    @app.get("/") #decorador, se ejecuta cuando se hace un get al / de mi app 
    def home(): 
        contenido = "mundo"
        return render_template("home.html", contenido=contenido)
    
    #Reigstro controller de issues
    app.register_blueprint(issue_blueprint)

    app.register_error_handler(404, handlers.not_found_error) #cuando encuentre un 404 ejecutar la funcion
    app.register_error_handler(500, handlers.internal_server_error)
    
    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()
        
    @app.cli.command(name="seeds")
    def seedsdb():
        seeds.run()

    return app