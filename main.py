from fastapi import FastAPI
# import database as db
from pydantic import BaseModel
import uvicorn
from prueba_database import Database as Sql

'''TERMINAL
Para crear un entorno virutal (Mac) -> python3 -m venv nombre_del_entorno_virtual
Para eliminar el entorno virtual (Mac)-> rm -rf nombre_del_entorno_virtual
para activarlo (estar en la terminal en la carpeta donde esta el entorno)(MAC) -> source nombre_entorno/bin/activate
para iniciar el servidor-> uvicorn main:app --reload
para parar el servidor control+c
para salir del entorno -> deactivate
'''
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
def entrar_dron(drone: Drone):
    try:
        x = sql.insertar_dron(drone.name, drone.chasis, drone.brazos, drone.helices, drone.bateria, drone.sensores,
                              drone.camara)
        if x == 0:
            return ('se ha insertado con exito')
        else:
            return x
    except Exception as e:
        return f"Algo no ha ido bien: {str(e)}"


@app.get("/muestra_drones")
def muestra_dron():
    return sql.mostrar_tabla()


@app.delete('/eliminar_dron/{name}')
def delete_dron(name: str):
    try:
        y = sql.elmiminar_dron(name)
        if y == 0:
            return f'Se ha eliminado con exito los drones con nombre: {name}'
        else:
            return y
    except Exception as e:
        return f"Algo no ha ido bien: {str(e)}"


@app.put("/update_name/{name},{name_viejo}")
def update_dron(name: str, name_viejo: str):
    try:
        z = sql.modificar_nombre(name, name_viejo)
        if z == 0:
            return 'Se ha cambiado con exito el nombre'
        else:
            return z
    except Exception as e:
        return f"Algo no ha ido bien: {str(e)}"


@app.put("/update_chasis/{name},{chasis}")
def update_chasis(name: str, chasis: str):
    try:
        z = sql.modificar_chasis(chasis, name)
        if z == 0:
            return 'Se ha cambiado con exito el chasis'
        else:
            return z
    except Exception as e:
        return f"Algo no ha ido bien: {str(e)}"


@app.put("/update_brazos/{name},{brazos}")
def update_brazos(name: str, brazos: int):
    try:
        z = sql.modificar_brazos(brazos, name)
        if z == 0:
            return 'Se ha cambiado con exito el numero de brazos'
        else:
            return z
    except Exception as e:
        return f"Algo no ha ido bien: {str(e)}"


@app.put("/update_helices/{name},{helices}")
def update_helices(name: str, helices: int):
    try:
        z = sql.modificar_helices(helices, name)
        if z == 0:
            return 'Se ha cambiado con exito el numero de helices'
        else:
            return z
    except Exception as e:
        return f"Algo no ha ido bien: {str(e)}"


@app.put("/update_bateria/{name},{bateria}")
def update_bateria(name: str, bateria: float):
    try:
        z = sql.modificar_bateria(bateria, name)
        if z == 0:
            return 'Se ha cambiado con exito la bateria'
        else:
            return z
    except Exception as e:
        return f"Algo no ha ido bien: {str(e)}"


@app.put("/update_sensores/{name},{sensores}")
def update_sensores(name: str, sensores: int):
    try:
        z = sql.modificar_sensores(sensores, name)
        if z == 0:
            return 'Se ha cambiado con exito el numero de sensores'
        else:
            return z
    except Exception as e:
        return f"Algo no ha ido bien: {str(e)}"


@app.put("/update_camara/{name},{camara}")
def update_cam(name: str, camara: str):
    try:
        z = sql.modificar_camara(camara, name)
        if z == 0:
            return 'Se ha cambiado con exito la camara'
        else:
            return z
    except Exception as e:
        return f"Algo no ha ido bien: {str(e)}"


# Esto es para que una vez se incia con el reload se vaya actualizando y no haya que meter en terminal el reload
# cada vez que hace un cambio.
if __name__ == "__main__":
    sql = Sql("localhost", "root", "password", "ATLAS_DB")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)