from app import app
from app.config import *
from app import eliminar

@cross_origin
@app.route('/eliminarNota', methods=['PUT'])
def actualizarNota():
    try:
        if request.method == 'PUT':
            dic = {
                'codigo' : request.json['codigo'],
                'estado' : request.json['estado']
            }
            return eliminar.actualizarNota(dic)

    except Exception as e:
        print(e)
        jsonify({'Informacion': e } )