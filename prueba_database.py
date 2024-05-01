
import pymysql


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
        #c.execute("INSERT INTO drones VALUES(%s,%s,%i,%i,%f,%i,%s)"%(name)%(chasis)%(brazos)%(helices)%(bateria)%(sensores)%(camara))
        c.execute("INSERT INTO drones VALUES (%s, %s, %s, %s, %s, %s, %s)", (name, chasis, brazos, helices, bateria, sensores, camara))
        conn.commit()
        conn.close()
        return 0
    except():
        return 1

def mostrar_tabla():
    conn = pymysql.connect(host='localhost', user='root',passwd='password',db='DRONES')
    c = conn.cursor() 
    c.execute("SELECT * FROM drones")
    data = c.fetchall()
    conn.commit()
    conn.close()
    print(data)
    return {'data':data}



insertar_dron('Prueba','carbono',4,4,67.6,8,'4k')   
mostrar_tabla()
