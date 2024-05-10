#sudo /usr/local/mysql/support-files/mysql.server start (Activar server desde terminal MAC)
#mysql -u root -p (Activar mySQL)
import pymysql

"""
LENGUAJE PARA MOVERSE EN TERMINAL mySQL
SHOW DATABASES;
USE nombre_database; (para entrar en esa base de datos)
SHOW TABLES;
DESCRIBE nombre_tabla; (enseña las propiedades de la tabla)
SELECT 
DELETE
UPDATE 
INSERT
exit (para salir)
"""

def initdb():
    conn = pymysql.connect(host='localhost', user='root',passwd='password',database='DRONES')
    c = conn.cursor()

    c.execute(''' CREATE TABLE IF NOT EXISTS drones (
            name TEXT,
            chasis TEXT,
            brazos INTEGER,
            helices INTEGER,
            bateria REAL,
            Sensores INTEGER,
            camara TEXT
            )''')
    conn.commit()
    conn.close()

def insertar_dron(name:str,chasis:str,brazos:int,helices:int,bateria:float,sensores:int,camara:str):
    try:
        conn = pymysql.connect(host='localhost', user='root',passwd='password',db='DRONES')
        c = conn.cursor()   
        c.execute("INSERT INTO drones VALUES (%s, %s, %s, %s, %s, %s, %s)", (name, chasis, brazos, helices, bateria, sensores, camara))
        conn.commit()
        conn.close()
        return 0
    except Exception as e:
        return f'Ha habido algun error en la base de datos: {str(e)}'

def mostrar_tabla():
    conn = pymysql.connect(host='localhost', user='root',passwd='password',db='DRONES')
    c = conn.cursor() 
    c.execute("SELECT * FROM drones")
    data = c.fetchall()
    conn.commit()
    conn.close()
    print(data)
    return {'data':data}


def elmiminar_dron(name:str):
    try:
        conn = pymysql.connect(host='localhost', user='root',passwd='password',db='DRONES')
        c = conn.cursor() 
        c.execute("DELETE FROM drones WHERE name = %s",(name,))
        if c.rowcount == 0:
            conn.commit()
            conn.close()
            return ("No hay ningún dron guardado con ese nombre.",401)
        else:
            conn.commit()
            conn.close()
            return 0
    except Exception as e:
        return f'Ha habido algun error en la base de datos: {str(e)}'


def modificar_nombre(name:str,nom_viejo:str):
    try:
        conn = pymysql.connect(host='localhost', user='root',passwd='password',db='DRONES')
        c = conn.cursor() 
        c.execute("UPDATE drones SET name=%s WHERE name=%s",(name,nom_viejo,))
        conn.commit()
        conn.close()
        return 0
    except Exception as e:
        return f'Ha habido algun error en la base de datos: {str(e)}'
    
def modificar_chasis(chasis:str, nombre:str):
    try:
        conn = pymysql.connect(host='localhost', user='root',passwd='password',db='DRONES')
        c = conn.cursor() 
        c.execute("UPDATE drones SET chasis=%s WHERE name=%s",(chasis,nombre,))
        conn.commit()
        conn.close()
        return 0
    except Exception as e:
        return f'Ha habido algun error en la base de datos: {str(e)}'

def modificar_brazos(brazos:int,name:str):
    try:
        conn = pymysql.connect(host='localhost', user='root',passwd='password',db='DRONES')
        c = conn.cursor() 
        c.execute("UPDATE drones SET brazos=%s WHERE name=%s",(brazos,name,))
        conn.commit()
        conn.close()
        return 0
    except Exception as e:
        return f'Ha habido algun error en la base de datos: {str(e)}'
    
def modificar_helices(helices:int,name:str):
    try:
        conn = pymysql.connect(host='localhost', user='root',passwd='password',db='DRONES')
        c = conn.cursor() 
        c.execute("UPDATE drones SET helices=%s WHERE name=%s",(helices,name,))
        conn.commit()
        conn.close()
        return 0
    except Exception as e:
        return f'Ha habido algun error en la base de datos: {str(e)}'
    
def modificar_bateria(bateria:float,name:str):
    try:
        conn = pymysql.connect(host='localhost', user='root',passwd='password',db='DRONES')
        c = conn.cursor() 
        c.execute("UPDATE drones SET bateria=%s WHERE name=%s",(bateria,name,))
        conn.commit()
        conn.close()
        return 0
    except Exception as e:
        return f'Ha habido algun error en la base de datos: {str(e)}'
    
def modificar_sensores(sensores:int,name:str):
    try:
        conn = pymysql.connect(host='localhost', user='root',passwd='password',db='DRONES')
        c = conn.cursor() 
        c.execute("UPDATE drones SET Sensores=%s WHERE name=%s",(sensores,name,))
        conn.commit()
        conn.close()
        return 0
    except Exception as e:
        return f'Ha habido algun error en la base de datos: {str(e)}'
    
def modificar_camara(cam:str,name:str):
    try:
        conn = pymysql.connect(host='localhost', user='root',passwd='password',db='DRONES')
        c = conn.cursor() 
        c.execute("UPDATE drones SET camara=%s WHERE name=%s",(cam,name))
        conn.commit()
        conn.close()
        return 0
    except Exception as e:
        return f'Ha habido algun error en la base de datos: {str(e)}'
    

#insertar_dron('Prueba','carbono',4,4,67.6,8,'4k')   
#mostrar_tabla()
