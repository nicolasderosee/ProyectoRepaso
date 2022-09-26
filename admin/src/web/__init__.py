from flask import Flask

def create_app(): #funcion que crea mi app 
    app = Flask(__name__)

    @app.get("/") #decorador, se ejecuta cuando se hace un get al / de mi app 
    def home(): 
        return "Hello World!"
    
    return app