from app import *
from app.config import *

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
                    'estado': resultado[10]
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
                    'estado': resultado[10]
                }
            )

            return jsonify(data)

    except Exception as e:
        print(e)
    finally:
        cur.close()

def consultarUsuario(codigoUsuario):
    pass

def consultarMateria(codigoMateria):
    pass

def consultarNotasEstudiante(codigoEstudiante):
    pass

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