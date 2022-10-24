from app import app
from app.config import *
from app import eliminar


@cross_origin
@app.route("/eliminarNota", methods=["PUT"])
def eliminarNota():
    try:
        if request.method == "PUT":
            dic = {"codigo": request.json["codigo"], "estado": request.json["estado"]}
            return eliminar.eliminarNota(dic)

    except Exception as e:
        print(e)
        jsonify({"Informacion": e})
