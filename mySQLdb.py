import pymysql

conn = pymysql.connect(db='DRONESmySQL.db')
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
        conn = pymysql.connect(host='localmysql', user='root',passwd='password',db='DRONESmySQL.db')
        c = conn.cursor()   
        c.execute("INSERT INTO drones VALUES(?,?,?,?,?,?,?)",(name,chasis,brazos,helices,bateria,sensores,camara))
        conn.commit()
        conn.close()
        return 0
    except():
        return 1

def mostrar_tabla():
    conn = pymysql.connect(db='DRONESmySQL.db')
    c = conn.cursor() 
    c.execute("SELECT * FROM drones")
    data = c.fetchall()
    conn.commit()
    conn.close()
    print(data)
    return {'data':data}



def elmiminar_dron(name:str):
    try:
        conn = pymysql.connect(host='localmysql', user='root',passwd='password',db='DRONESmySQL.db')
        c = conn.cursor() 
        c.execute("DELETE FROM drones WHERE name = ?",(name,))
        conn.commit()
        conn.close()
        return 0
    except():
        return 1
    
def modificar_nombre(name:str,nom_viejo:str):
    try:
        conn = pymysql.connect(host='localmysql', user='root',passwd='password',db='DRONESmySQL.db')
        c = conn.cursor() 
        c.execute("UPDATE drones SET name=? WHERE name=?",(name,nom_viejo,))
        conn.commit()
        conn.close()
        return 0
    except():
        return 1
    
mostrar_tabla()