from flask import Blueprint
from flask import render_template

issue_blueprint = Blueprint("issues", __name__, url_prefix="/consultas")

@issue_blueprint.get("/")

def issue_index():
    
    issues = [  
        {
            "id": 1,
            "user": "José",
            "title": "Mi computadora no funciona.",
            "description": "Mi departamente me compró una nueva computadora y necesito configurarla con todos mis emails y documentos de mi vieja computadora.",
            "status": "new",
        },
        {
            "id": 2,
            "user": "María",
            "title": "No puedo obtener mis emails.",
            "description": "Estoy tratando de acceder a mi correo desde casa, pero no puedo obtenerlos. Estoy tratando con Outlook en mi casa pero en la oficina tengo Thunderbird.",
            "status": "in_progress",
        },
        {
            "id": 3,
            "user": "Rubén",
            "title": "No puedo imprimir",
            "description": "Cada vez que trato de imprimir mi presentación el programa se cierra. Esto sólo me pasa con PowerPoint en Word puedo imprimir. Ya me aseguré que la impresora está prendida. Tengo una HP LaserJet 5.",
            "status": "done",
        },
    ]

    return render_template("issues/index.html", issues=issues)