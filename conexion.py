from logger_base import log
from psycopg2 import pool
import sys
from colorama import *

class Conexion:

    #Datos estaticos de conexion 

    _DATABASE = 'test_db'
    _USERNAME = '' #Usuario local 
    _PASSWORD = '' #Cotraseña Local
    _HOST = '127.0.0.1'
    _DB_PORT = '5432'
    _MIN_CON = 1
    _MAX_CON = 5  
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None: # Se cra el pool si no esta creado
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON, host = cls._HOST,
                                                                                  user = cls._USERNAME,
                                                                                  password = cls._PASSWORD,
                                                                                  port = cls._DB_PORT,
                                                                                  database = cls._DATABASE)
                #log.debug(f"{Fore.GREEN}CREACION DEL POOL EXITOSA:{Style.RESET_ALL} {cls._pool}" )
                
                return cls._pool
            except Exception as e:
                log.error(f"{Fore.RED}OCURRIO UN ERROR AL CREAR EL POOL:{Style.RESET_ALL} {e}" )
                sys.exit() # si hay error solo se cancela el llamado al pool
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn() # Despues de obtener el pool, se conecta 
        #log.debug(f"{Fore.GREEN}SE OBTUVO CONEXION CON EL POOL:{Style.RESET_ALL} {conexion}")
        return conexion

    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)  # despues de usarse la conexion se libera ese espacio
        #log.debug(f"{Fore.LIGHTBLUE_EX}SE LIBERO CONEXION EN EL POOL:{Style.RESET_ALL} {conexion}")

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall() # se cierra oas las conexiones 
        #log.debug(f"{Fore.LIGHTMAGENTA_EX}SE CERRARON TODAS LAS CONEXIONES{Style.RESET_ALL}")
    
if __name__ == "__main__":
    #si ejecutamos esto podemos ver que el pool se crea una sola ves y despues las instrucciones
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()

