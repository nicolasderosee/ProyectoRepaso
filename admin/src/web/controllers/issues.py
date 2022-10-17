#controllers de issue
from flask import Blueprint
from flask import render_template
from src.core import board

issue_blueprint = Blueprint("issues", __name__, url_prefix="/consultas")

@issue_blueprint.get("/")
def issue_index():

    issues = board.list_issues() #obtengo los issues del modelo 
    
    return render_template("issues/index.html", issues=issues) 
    
    #toma este archivo y se lo manda al template 
    #combina vista con modelo y se lo retorna al browser 