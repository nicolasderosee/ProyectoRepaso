from click import password_option
from src.core import auth
from src.core import board
from src.core import auth 

def run():
    issue1 = board.create_issue(
        email="jose@gmail.com",
        title="Mi computadora no funciona.",
        description="Mi departamento me compro una nueva compu y necesito configurarla",
        status="new",
    )

    issue2=board.create_issue(
        email="maria@gmail.com",
        title="No puedo obtener mis emails.",
        description="Estoy tratando de acceder a mi correo pero no puedo",
        status="in_progress",
    )

    issue3=board.create_issue(
        email="orlando@gmail.com",
        title="No puedo imprimir.",
        description="Estoy tratando imprimir pero salta error",
        status="done",
    )

    jose= auth.create_user(email="jose@gmail.com", password="1234")
    maria=auth.create_user(email="maria@gmail.com", password="1111")
    orlando=auth.create_user(email="orlando@gmail.com", password="2222")
    agus=auth.create_user(email="agus@gmail.com", password="2252")