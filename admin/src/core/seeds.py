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

    fede= auth.create_user(email="fede@gmail.com", password="1234")
    dolores=auth.create_user(email="dolores@gmail.com", password="1111")
    ariana=auth.create_user(email="ariana@gmail.com", password="2222")


    label1 = board.create_label(
        title="Urgente",
        description="Issues que tienen que resolverse dentro de 24hs"
    )

    label2 = board.create_label(
        title="Importantes",
        description="Issues de alta prioridad"
    )

    label3 = board.create_label(
        title="Soporte",
        description="Issues relacionados con soporte técnico",
    )

    label4 = board.create_label(
        title="Ventas",
        description="Issues relacionados con el área de ventas",
    )


    board.assign_labels(issue1, [label1,label2])
    board.assign_labels(issue2, [label3,label4])
    board.assign_labels(issue3, [label1,label4])

    board.assign_user(issue1, fede)
    board.assign_user(issue2, dolores)
    board.assign_user(issue3, ariana)