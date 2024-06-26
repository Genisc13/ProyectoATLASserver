# sudo /usr/local/mysql/support-files/mysql.server start (Activar server desde terminal MAC)
# mysql -u root -p (Activar mySQL)
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


class Database:
    def __init__(self, host, user, password, name):
        super().__init__()
        self.database_host = host
        self.database_user = user
        self.database_password = password
        self.database_name = name
        self.conn = pymysql.connect(host=self.database_host, user=self.database_user, passwd=self.database_password)
        c = self.conn.cursor()
        c.execute(f"CREATE DATABASE IF NOT EXISTS {self.database_name}")
        self.conn = pymysql.connect(host=self.database_host, user=self.database_user, passwd=self.database_password,
                                    database=self.database_name)
        c = self.conn.cursor()
        c.execute(''' CREATE TABLE IF NOT EXISTS drones (
                  name TEXT,
                  chasis TEXT,
                  brazos INTEGER,
                  helices INTEGER,
                  bateria REAL,
                  Sensores INTEGER,
                  camara TEXT
                  )''')
        c.execute(''' CREATE TABLE IF NOT EXISTS usuarios (
                  nombre TEXT,
                  password TEXT,
                  mail TEXT
                  )''')
        self.conn.commit()
        self.conn.close()

    def insertar_dron(self, name: str, chasis: str, brazos: int, helices: int, bateria: float, sensores: int,
                      camara: str):
        try:
            self.conn = pymysql.connect(host=self.database_host, user=self.database_user, passwd=self.database_password,
                                        database=self.database_name)
            c = self.conn.cursor()
            c.execute("INSERT INTO drones VALUES (%s, %s, %s, %s, %s, %s, %s)",
                      (name, chasis, brazos, helices, bateria, sensores, camara))
            self.conn.commit()
            self.conn.close()
            return 0
        except Exception as e:
            return f'Ha habido algun error en la base de datos: {str(e)}'
        
    def check_usuario(self,name:str,constraseña:str):
        try:
            self.conn = pymysql.connect(host=self.database_host, user=self.database_user, passwd=self.database_password,
                                        database=self.database_name)
            c = self.conn.cursor()
            c.execute('SELECT * FROM usuarios WHERE nombre =" %s"',(name,))
            
            result = c.fetchall()
            print(result)
            if result[0] == name and result[1] == constraseña:
                return "El usuario es correcto puede entrar"
            else:
                return "El nombre o la contraseña estan mal"
        except Exception as e:
            return f'Ha habido algun error en la base de datos: {str(e)}'
        

    def insertar_usuarios(self, name: str, password: str, mail: str):
        try:
            self.conn = pymysql.connect(host=self.database_host, user=self.database_user, passwd=self.database_password,
                                        database=self.database_name)
            c = self.conn.cursor()
            
            x = c.execute('SELECT * FROM usuarios WHERE nombre =" %s"',(name,))
            
            if 0 < x:
                return "Ya existe una cuenta con ese nombre"
            else:
                c.execute('INSERT INTO usuarios VALUES ("%s", "%s", "%s")',
                        (name, password, mail))
                
                self.conn.commit()
                self.conn.close()
                return 0
        except Exception as e:
            return f'Ha habido algun error en la base de datos: {str(e)}'
        
    def mostrar_tabla(self):
        self.conn = pymysql.connect(host=self.database_host, user=self.database_user, passwd=self.database_password,
                                    database=self.database_name)
        c = self.conn.cursor()
        c.execute("SELECT * FROM drones")
        data = c.fetchall()
        self.conn.commit()
        self.conn.close()
        print(data)
        return {'data': data}

    def elmiminar_dron(self, name: str):
        try:
            self.conn = pymysql.connect(host=self.database_host, user=self.database_user, passwd=self.database_password,
                                        database=self.database_name)
            c = self.conn.cursor()
            c.execute("DELETE FROM drones WHERE name = %s", (name,))
            if c.rowcount == 0:
                self.conn.commit()
                self.conn.close()
                return ("No hay ningún dron guardado con ese nombre.")
            else:
                self.conn.commit()
                self.conn.close()
                return 0
        except Exception as e:
            return f'Ha habido algun error en la base de datos: {str(e)}'

    def modificar_nombre(self, name: str, nom_viejo: str):
        try:
            self.conn = pymysql.connect(host=self.database_host, user=self.database_user, passwd=self.database_password,
                                        database=self.database_name)
            c = self.conn.cursor()
            c.execute("UPDATE drones SET name=%s WHERE name=%s", (name, nom_viejo,))
            self.conn.commit()
            self.conn.close()
            return 0
        except Exception as e:
            return f'Ha habido algun error en la base de datos: {str(e)}'

    def modificar_chasis(self, chasis: str, nombre: str):
        try:
            self.conn = pymysql.connect(host=self.database_host, user=self.database_user, passwd=self.database_password,
                                        database=self.database_name)
            c = self.conn.cursor()
            c.execute("UPDATE drones SET chasis=%s WHERE name=%s", (chasis, nombre,))
            self.conn.commit()
            self.conn.close()
            return 0
        except Exception as e:
            return f'Ha habido algun error en la base de datos: {str(e)}'

    def modificar_brazos(self, brazos: int, name: str):
        try:
            self.conn = pymysql.connect(host=self.database_host, user=self.database_user, passwd=self.database_password,
                                        database=self.database_name)
            c = self.conn.cursor()
            c.execute("UPDATE drones SET brazos=%s WHERE name=%s", (brazos, name,))
            self.conn.commit()
            self.conn.close()
            return 0
        except Exception as e:
            return f'Ha habido algun error en la base de datos: {str(e)}'

    def modificar_helices(self, helices: int, name: str):
        try:
            self.conn = pymysql.connect(host=self.database_host, user=self.database_user, passwd=self.database_password,
                                        database=self.database_name)
            c = self.conn.cursor()
            c.execute("UPDATE drones SET helices=%s WHERE name=%s", (helices, name,))
            self.conn.commit()
            self.conn.close()
            return 0
        except Exception as e:
            return f'Ha habido algun error en la base de datos: {str(e)}'

    def modificar_bateria(self, bateria: float, name: str):
        try:
            self.conn = pymysql.connect(host=self.database_host, user=self.database_user, passwd=self.database_password,
                                        database=self.database_name)
            c = self.conn.cursor()
            c.execute("UPDATE drones SET bateria=%s WHERE name=%s", (bateria, name,))
            self.conn.commit()
            self.conn.close()
            return 0
        except Exception as e:
            return f'Ha habido algun error en la base de datos: {str(e)}'

    def modificar_sensores(self, sensores: int, name: str):
        try:
            self.conn = pymysql.connect(host=self.database_host, user=self.database_user, passwd=self.database_password,
                                        database=self.database_name)
            c = self.conn.cursor()
            c.execute("UPDATE drones SET Sensores=%s WHERE name=%s", (sensores, name,))
            self.conn.commit()
            self.conn.close()
            return 0
        except Exception as e:
            return f'Ha habido algun error en la base de datos: {str(e)}'

    def modificar_camara(self, cam: str, name: str):
        try:
            self.conn = pymysql.connect(host=self.database_host, user=self.database_user, passwd=self.database_password,
                                        database=self.database_name)
            c = self.conn.cursor()
            c.execute("UPDATE drones SET camara=%s WHERE name=%s", (cam, name))
            self.conn.commit()
            self.conn.close()
            return 0
        except Exception as e:
            return f'Ha habido algun error en la base de datos: {str(e)}'

    # insertar_dron('Prueba','carbono',4,4,67.6,8,'4k')
    # mostrar_tabla()

#var = Database("localhost", "root", "password", "atlas_db")
#var.insertar_usuarios("'iker'", 'pas', 'algo@algo')
#var.check_usuario('str','str')