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
                resultado
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
                resultado
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
            
            """ aux = {
                    'id': resultado[0],
                    'tipo_usuario': resultado[1],
                    'codigo': resultado[2],
                    'username': resultado[3],
                    'password': resultado[4],
                    'fecha_creacion': resultado[5],
                    'estado': resultado[6],
                    'nota': resultado[7]
                } """
            data.append(resultado)

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
                resultado
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
                resultado
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
                resultado
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
                resultado
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
                resultado
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
                resultado
            )

        return jsonify(data)

    except Exception as e:
        print(e)
    finally:
        cur.close()

## PARCIAL 2

def accionParcial(accion):
    opciones = {
        1: 'call obtenerEstudiantesMayorNota()',
        2: 'call obtenerUsuariosProfesores()',
        3: 'call obtenerNombreProfesor_Nota()',
        4: 'call obtenerEst_Pro_Mat_TipoNota()',
        5: 'call obtenerUsuario_TipoNota()',
        6: 'call obtenerEst_Pro_Mat_Curso()',
        7: 'call obtenerPromedioMat()',
        8: 'call obtenerConteoEstudiantes_Curso()',
        9: 'call sumaCalificaciones_Materia()',
        10: 'call obtenerUserPw_Prof_Mat()',
        11: 'call est_prof_mat_esp_notas()',
        12: 'call obtenerProcDobleCondicional()'
        }
    return opciones[accion]

def consultaParcial2(n):
    try:
        cur = mysql.connection.cursor()
        sql = accionParcial(n)
        cur.execute(sql)
        res = cur.fetchall()
        data = []
        for resultado in res:
            data.append(
                resultado
            )

        return jsonify(data)

    except Exception as e:
        print(e)
    finally:
        cur.close()