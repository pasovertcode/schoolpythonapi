from app import *
from app.config import *


## Notas

def agregarNota(dicNotas):
    try:
        cur = mysql.connection.cursor()
        sql = "call agregarNota('{0}','{1}','{2}','{3}','{4}','{5}','{6}',{7},'{8}','{9}')"
        cur.execute(sql.format(
            dicNotas['codigo'],
            dicNotas['tipo'],
            dicNotas['periodo'],
            dicNotas['nid_profesor'],
            dicNotas['codigo_asignatura'],
            dicNotas['curso'],
            dicNotas['nid_estudiante'],
            dicNotas['calificacion'],
            dicNotas['anotacion'],
            dicNotas['estado']
        ))
        mysql.connection.commit()
        return jsonify({"Informacion": "Registro Exitoso."})


    except Exception as e:
        print(e)
        return jsonify({'info': e})
    finally:
        cur.close()

