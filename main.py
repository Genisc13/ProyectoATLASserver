from fastapi import FastAPI
import database as db
from pydantic import BaseModel
import uvicorn
import prueba_database

app = FastAPI()

class Drone(BaseModel):
    name: str
    chasis: str
    brazos: int
    helices: int
    bateria: float
    sensores: int
    camara: str


@app.get("/")
def root():
    return 'esto va?'

@app.post('/add_drones')
def entrar_dron(drone:Drone):
    try:
        db.insertar_dron(drone.name,drone.chasis,drone.brazos,drone.helices,drone.bateria,drone.sensores,drone.camara)  
        return('se ha insertado con exito') 
    except Exception as e:
        return f"Algo no ha ido bien: {str(e)}"
    
@app.get("/muestra_drones")
def muestra_dron():
    return db.mostrar_tabla()

@app.delete('/eliminar_dron/{name}')
def delete_dron(name:str):
    try:
        db.elmiminar_dron(name)
        return f'Se ha eliminado con exito los drones con nombre: {name}'
    except Exception as e:
        return f"Algo no ha ido bien: {str(e)}"
    

@app.put("/update_dron/{name},{name_viejo}")
def update_dron(name:str,name_viejo:str):
    try:
        db.modificar_nombre(name,name_viejo)
        return 'Se ha cambiado con exito el nombre'
    except Exception as e:
        return f"Algo no ha ido bien: {str(e)}"
    


#def setup():
 #   conn = sqlite3.connect('DRONES.db')
  #  c = conn.cursor()

   # c.execute(''' CREATE TABLE IF NOT EXISTS drones (
    #          name TEXT,
     #         chasis TEXT,
      #        brazos INTEGER,
       #       helices INTEGER,
        #      bateria REAL,
         #     sensores INTEGER,
          #    camara TEXT
           #   )''')
    
  #  conn.commit()
   # conn.close()


if __name__ == "__main__":
    #setup()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)