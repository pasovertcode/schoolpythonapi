from app import *
from app.config import *


def eliminarNota(dic):
    try:
        cur = mysql.connection.cursor()
        sql = "call cambiarEstadoNota('{0}','{1}')"
        cur.execute(sql.format(dic["codigo"], "desactivado"))
        mysql.connection.commit()
        return jsonify({"Informacion": "Registro Eliminado."})

    except Exception as e:
        print(e)
        return jsonify({"info": e})
    finally:
        cur.close()
