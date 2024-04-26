import sqlite3

conn = sqlite3.connect('DRONES.db')
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
        conn = sqlite3.connect('DRONES.db')
        c = conn.cursor()   
        c.execute("INSERT INTO drones VALUES(?,?,?,?,?,?,?)",(name,chasis,brazos,helices,bateria,sensores,camara))
        conn.commit()
        conn.close()
        return 0
    except():
        return 1
    


def mostrar_tabla():
    conn = sqlite3.connect('DRONES.db')
    c = conn.cursor() 
    c.execute("SELECT * FROM drones")
    data = c.fetchall()
    conn.commit()
    conn.close()
    print(data)
    return {'data':data}


def elmiminar_dron(name:str):
    try:
        conn = sqlite3.connect('DRONES.db')
        c = conn.cursor() 
        c.execute("DELETE FROM drones WHERE name = ?",(name,))
        conn.commit()
        conn.close()
        return 0
    except():
        return 1

def modificar_nombre(name:str,nom_viejo:str):
    try:
        conn = sqlite3.connect('DRONES.db')
        c = conn.cursor() 
        c.execute("UPDATE drones SET name=? WHERE name=?",(name,nom_viejo,))
        conn.commit()
        conn.close()
        return 0
    except():
        return 1
    
def modificar_chasis(chasis:str, nom_viejo:str):
    try:
        conn = sqlite3.connect('DRONES.db')
        c = conn.cursor() 
        c.execute("UPDATE drones SET chasis=? WHERE name=?",(chasis,nom_viejo))
        conn.commit()
        conn.close()
        return 0
    except():
        return 1
    
def modificar_brazos(brazos:int,braz_vie:int):
    try:
        conn = sqlite3.connect('DRONES.db')
        c = conn.cursor() 
        c.execute("UPDATE drones SET brazos=? WHERE brazos=?",(brazos,braz_vie))
        conn.commit()
        conn.close()
        return 0
    except():
        return 1
    
def modificar_helices(helices:int,helix_vieja:int):
    try:
        conn = sqlite3.connect('DRONES.db')
        c = conn.cursor() 
        c.execute("UPDATE drones SET helices=? WHERE helices=?",(helices,helix_vieja,))
        conn.commit()
        conn.close()
        return 0
    except():
        return 1
    
def modificar_bateria(bateria:float,bat_vieja:float):
    try:
        conn = sqlite3.connect('DRONES.db')
        c = conn.cursor() 
        c.execute("UPDATE drones SET bateria=? WHERE bateria=?",(bateria,bat_vieja,))
        conn.commit()
        conn.close()
        return 0
    except():
        return 1
    
def modificar_sensores(sensores:int,sen_viejo:str):
    try:
        conn = sqlite3.connect('DRONES.db')
        c = conn.cursor() 
        c.execute("UPDATE drones SET Sensores=? WHERE Sensores=?",(sensores,sen_viejo,))
        conn.commit()
        conn.close()
        return 0
    except():
        return 1
    
def modificar_camara(cam:str,vieja_cam:str):
    try:
        conn = sqlite3.connect('DRONES.db')
        c = conn.cursor() 
        c.execute("UPDATE drones SET camara=? WHERE camara=?",(cam,vieja_cam))
        conn.commit()
        conn.close()
        return 0
    except():
        return 1
    
#insertar_dron('drone2','fibra',4,8,98,12,'SONY')
#elmiminar_dron('ring')
#modificar_nombre('hassgrober','grober')
mostrar_tabla()


