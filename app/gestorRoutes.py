from app import app
from app.config import *
from app import consultas
from app import eliminar
from app import agregar
from app import actualizar

## Notas

@cross_origin
@app.route('/managerNotas/<id>', methods=['GET'])
@app.route('/managerNotas/buscar/<cod_estudiante>', methods=['GET'])
@app.route('/managerNotas', methods=['GET','POST','PUT'])
def managerNotas(cod_estudiante = None, id = None):
        try:
            
            if id != None:
                id = int(id)
                if id >= 1 and id <= 12:
                    return consultas.consultaParcial2(id)
                return jsonify({'Información': 'El ID debe ser entre 1 y 12.'})
                
            if cod_estudiante == None:
                if request.method == 'GET':
                    return jsonify({'Información': 'Acción no valida.'})

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
                if request.method == 'PUT':
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
                    return actualizar.actualizarNota(dicNota)
                if request.method == 'DELETE':
                    dic = {
                    'codigo' : request.json['codigo'],
                    'estado' : request.json['estado']
                    }
                    return eliminar.eliminarNota(dic)

            if request.method == 'GET':
                mensaje = consultas.consultarNotasEstudiante(cod_estudiante)
                return mensaje
            
            return f"<h1> {cod_estudiante} </h1>"
        except Exception as e:
            print(e)
            return jsonify({'Informacion': e } )
    




## Profesor


@cross_origin
@app.route('/managerProfesor/<id_profesor>', methods=['GET'])
@app.route('/managerProfesor', methods=['GET','POST','PUT'])
def managerProfesor(id_profesor = None):
    print(id_profesor)
    return f"<h1> {id_profesor} </h1>"


## Estudiante


@cross_origin
@app.route('/managerEstudiante/<cod_estudiante>', methods=['GET'])
@app.route('/managerEstudiante', methods=['GET','POST','PUT'])
def managerEstudiante(cod_estudiante = None):
    print(cod_estudiante)
    return f"<h1> {cod_estudiante} </h1>"

