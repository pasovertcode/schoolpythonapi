from app import app
from app.config import *
from app import agregar

@cross_origin
@app.route('/addNota', methods=['POST'])
def addNota():
    try:
        if request.method == 'POST':
            dicNota = {
                'codigo' : request.json['codigo'],
                'tipo' : request.json['tipo'],
                'periodo' : request.json['periodo'],
                'nid_profesor' : request.json['nid_profesor'],
                'codigo_asignatura' : request.json['codigo_asignatura'],
                'curso' : request.json['curso'],
                'nid_estudiante' : request.json['nid_estudiante'],
                'calificacion' : request.json['calificacion'],
                'anotacion' : request.json['anotacion'],
                'estado' : request.json['estado']
            }
            return agregar.agregarNota(dicNota)

    except Exception as e:
        print(e)
        jsonify({'Informacion': e } )