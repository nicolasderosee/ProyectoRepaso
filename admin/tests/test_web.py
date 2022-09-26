from http import client
from operator import truediv
from web import create_app

app = create_app()
app.testing = True
client = app.test_client()

def test_home():
    response = client.get("/")
    assert b"Hello World!" in response.data #valida que hello world se enecuntre en la respuesta