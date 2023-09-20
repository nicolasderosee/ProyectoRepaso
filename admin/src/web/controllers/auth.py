from flask import Blueprint
from flask import render_template

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

@auth_blueprint.get("/")
def login():
    return render_template("auth/login.html")

@auth_blueprint.post("/authenticate")
def authenticate():
    pass

@auth_blueprint.get("/logout")
def logout():
    pass