from app import app
from app.config import *
from app import consultas


@app.route("/")
def inicio():
    return "<h1>Hola Mundo</h1>"


## Usuario


@cross_origin
@app.route("/obtenerUsuario/<codigoUsuario>", methods=["GET"])
def obtenerUsuario(codigoUsuario):
    mensaje = consultas.consultarUsuario(codigoUsuario)
    return mensaje


@cross_origin
@app.route("/obtenerUsuarios", methods=["GET"])
def obtenerUsuarios():
    mensaje = consultas.consultarUsuarios()
    return mensaje


## Estudiante


@cross_origin
@app.route("/obtenerEstudiante/<codigoEstudiante>", methods=["GET"])
def obtenerEstudiante(codigoEstudiante):
    mensaje = consultas.consultarEstudiante(codigoEstudiante)
    return mensaje


@cross_origin
@app.route("/obtenerEstudiantes", methods=["GET"])
def obtenerEstudiantes():
    mensaje = consultas.consultarEstudiantes()
    return mensaje


## Profesor


@cross_origin
@app.route("/obtenerProfesor/<codigoProfesor>", methods=["GET"])
def obtenerProfesor(codigoProfesor):
    mensaje = consultas.consultarProfesor(codigoProfesor)
    return mensaje


@cross_origin
@app.route("/obtenerProfesores", methods=["GET"])
def obtenerProfesores():
    mensaje = consultas.consultarProfesores()
    return mensaje


## Materias / Asignaturas


@cross_origin
@app.route("/obtenerMateria/<codigoMateria>", methods=["GET"])
def obtenerMateria(codigoMateria):
    mensaje = consultas.consultarMateria(codigoMateria)
    return mensaje


@cross_origin
@app.route("/obtenerMaterias", methods=["GET"])
def obtenerMaterias():
    mensaje = consultas.consultarMaterias()
    return mensaje


@cross_origin
@app.route("/obtenerNotasEstudiante/<codigoEstudiante>", methods=["GET"])
def obtenerNotasEstudiante(codigoEstudiante):
    mensaje = consultas.consultarNotasEstudiante(codigoEstudiante)
    return mensaje
