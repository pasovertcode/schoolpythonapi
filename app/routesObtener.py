from app import app
from app.config import *
from app import consultas

@app.route('/')
def inicio():
    return "<h1>Hola Mundo</h1>"

@cross_origin
@app.route('/obtenerUsuario/<codigoUsuario>', methods=['GET'])
def obtenerUsuario(codigoUsuario):
    mensaje = f"<h1>El codigo es: {codigoUsuario} </h1>"
    return mensaje

@cross_origin
@app.route('/obtenerEstudiante/<codigoEstudiante>', methods=['GET'])
def obtenerEstudiante(codigoEstudiante):
    mensaje = f"<h1>El codigo es: {codigoEstudiante} </h1>"
    return mensaje

@cross_origin
@app.route('/obtenerProfesor/<codigoProfesor>', methods=['GET'])
def obtenerProfesor(codigoProfesor):
    mensaje = consultas.consultarProfesor(codigoProfesor)
    return mensaje

@cross_origin
@app.route('/obtenerMateria/<codigoMateria>', methods=['GET'])
def obtenerMateria(codigoMateria):
    mensaje = f"<h1>El codigo es: {codigoMateria} </h1>"
    return mensaje

@cross_origin
@app.route('/obtenerNotasEstudiante/<codigoEstudiante>', methods=['GET'])
def obtenerNotasEstudiante(codigoEstudiante):
    mensaje = f"<h1>El codigo es: {codigoEstudiante} </h1>"
    return mensaje




