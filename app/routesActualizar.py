from app import app
from app.config import *
from app import actualizar


@cross_origin
@app.route("/actualizarNota", methods=["PUT"])
def actualizarNota():
    try:
        if request.method == "PUT":
            dicNota = {
                "codigo": request.json["codigo"],
                "tipo": request.json["tipo"],
                "periodo": request.json["periodo"],
                "nid_profesor": request.json["nid_profesor"],
                "codigo_asignatura": request.json["codigo_asignatura"],
                "curso": request.json["curso"],
                "nid_estudiante": request.json["nid_estudiante"],
                "calificacion": request.json["calificacion"],
                "anotacion": request.json["anotacion"],
                "estado": request.json["estado"],
            }
            return actualizar.actualizarNota(dicNota)

    except Exception as e:
        print(e)
        jsonify({"Informacion": e})
