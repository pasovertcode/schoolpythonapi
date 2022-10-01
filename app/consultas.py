from app import *
from app.config import *

## Consulta Estudiante
def consultarEstudiantes():
    try:
        cur = mysql.connection.cursor()
        sql = "call obtenerAllEstudiantes()"
        cur.execute(sql)
        res = cur.fetchall()
        data = []
        for resultado in res:
            data.append(
                {
                    'id': resultado[0],
                    'tipo_id': resultado[1],
                    'codigo': resultado[2],
                    'nacionalidad': resultado[3],
                    'nombres': resultado[4],
                    'apellidos': resultado[5],
                    'fecha_nacimiento': resultado[6],
                    'estado': resultado[9]
                }
            )

        return jsonify(data)

    except Exception as e:
        print(e)
    finally:
        cur.close()

def consultarEstudiante(codigoEstudiante):
    try:
        cur = mysql.connection.cursor()
        sql = "call obtenerEstudiante('{0}')"
        cur.execute(sql.format(codigoEstudiante))
        res = cur.fetchall()
        data = []
        for resultado in res:
            data.append(
                {
                    'id': resultado[0],
                    'tipo_id': resultado[1],
                    'codigo': resultado[2],
                    'nacionalidad': resultado[3],
                    'nombres': resultado[4],
                    'apellidos': resultado[5],
                    'fecha_nacimiento': resultado[6],
                    'estado': resultado[9]
                }
            )

        return jsonify(data)

    except Exception as e:
        print(e)
    finally:
        cur.close()


## Consulta Usuario

def consultarUsuarios():
    try:
        cur = mysql.connection.cursor()
        sql = "call obtenerUsuarios()"
        cur.execute(sql)
        res = cur.fetchall()
        data = []
        for resultado in res:
            print(resultado)
            aux = {
                    'id': resultado[0],
                    'tipo_usuario': resultado[1],
                    'codigo': resultado[2],
                    'username': resultado[3],
                    'password': resultado[4],
                    'fecha_creacion': resultado[5],
                    'estado': resultado[6],
                    'nota': resultado[7]
                }
            data.append(aux)

        return jsonify(data)

    except Exception as e:
        print(e)
    finally:
        cur.close()


def consultarUsuario(codigoUsuario):
    try:
        cur = mysql.connection.cursor()
        sql = "call obtenerUsuario('{0}')"
        cur.execute(sql.format(codigoUsuario))
        res = cur.fetchall()
        data = []
        for resultado in res:
            data.append(
                {
                    'id': resultado[0],
                    'tipo_usuario': resultado[1],
                    'codigo': resultado[2],
                    'username': resultado[3],
                    'password': resultado[4],
                    'fecha_creacion': resultado[5],
                    'estado': resultado[6],
                    'nota': resultado[7]
                }
            )

        return jsonify(data)

    except Exception as e:
        print(e)
    finally:
        cur.close()


## Consulta Materia


def consultarMateria(codigoMateria):
    try:
        cur = mysql.connection.cursor()
        sql = "call obtenerMateria('{0}')"
        cur.execute(sql.format(codigoMateria))
        res = cur.fetchall()
        data = []
        for resultado in res:
            data.append(
                {
                    'id': resultado[0],
                    'codigo': resultado[1],
                    'nombre': resultado[2],
                    'estado': resultado[3]
                }
            )

        return jsonify(data)

    except Exception as e:
        print(e)
    finally:
        cur.close()

def consultarMaterias():
    try:
        cur = mysql.connection.cursor()
        sql = "call obtenerMaterias()"
        cur.execute(sql)
        res = cur.fetchall()
        data = []
        for resultado in res:
            data.append(
                {
                    'id': resultado[0],
                    'codigo': resultado[1],
                    'nombre': resultado[2],
                    'estado': resultado[3]
                }
            )

        return jsonify(data)

    except Exception as e:
        print(e)
    finally:
        cur.close()


## Consulta nota


def consultarNotasEstudiante(codigoEstudiante):
    try:
        cur = mysql.connection.cursor()
        sql = "call obtenerNotasEstudiante('{0}')"
        cur.execute(sql.format(codigoEstudiante))
        res = cur.fetchall()
        data = []
        for resultado in res:
            data.append(
                {
                    'id': resultado[0],
                    'codigo': resultado[1],
                    'periodo': resultado[2],
                    'tipo': resultado[10],
                    'nombre_profesor': resultado[3],
                    'asignatura': resultado[4],
                    'curso': resultado[5],
                    'nombre_Estudiante': resultado[6],
                    'calificacion': resultado[7],
                    'anotacion': resultado[8],
                    'estado': resultado[9]
                }
            )

        return jsonify(data)

    except Exception as e:
        print(e)
    finally:
        cur.close()


## Consulta Profesor


def consultarProfesores():
    try:
        cur = mysql.connection.cursor()
        sql = "call obtenerProfesores()"
        cur.execute(sql)
        res = cur.fetchall()
        data = []
        for resultado in res:
            data.append(
                {
                    'id': resultado[0],
                    'tipo_id': resultado[1],
                    'codigo': resultado[2],
                    'nacionalidad': resultado[3],
                    'nombres': resultado[4],
                    'apellidos': resultado[5],
                    'fecha_nacimiento': resultado[6],
                    'estado': resultado[10]
                }
            )

        return jsonify(data)

    except Exception as e:
        print(e)
    finally:
        cur.close()


def consultarProfesor(codigoProfesor):
    try:
        cur = mysql.connection.cursor()
        sql = "call obtenerProfesor('{0}')"
        cur.execute(sql.format(codigoProfesor))
        res = cur.fetchall()
        data = []
        for resultado in res:
            data.append(
                {
                    'id': resultado[0],
                    'tipo_id': resultado[1],
                    'codigo': resultado[2],
                    'nacionalidad': resultado[3],
                    'nombres': resultado[4],
                    'apellidos': resultado[5],
                    'fecha_nacimiento': resultado[6],
                    'estado': resultado[10]
                }
            )

        return jsonify(data)

    except Exception as e:
        print(e)
    finally:
        cur.close()