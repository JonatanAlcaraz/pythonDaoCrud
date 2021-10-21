from logger_base import log
from conexion import Conexion 
from colorama import *
class CursorDelPool:

    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        #log.debug("Inicio del metodo WITH __enter__")
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self,tipo_excepcion,valor_excepcion,detalle_excepcion):
        #log.debug("Se ejecuta metodo exit")
        if valor_excepcion:
            self._conexion.rollback()
            log.debug(f"{Fore.RED}OCURRIO UNA EXCEPCION:{Style.RESET_ALL} {valor_excepcion , tipo_excepcion , detalle_excepcion}")
        else:
            self._conexion.commit()
            #log.debug(f"{Fore.YELLOW}SE HACE COMMIT DE LA TRANSACCION{Style.RESET_ALL}")

        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == "__main__":
     
     
    with CursorDelPool() as cursor:
        cursor.execute('SELECT * FROM persona')
        registros = cursor.fetchall()
        for registro in registros:
            log.debug(registro)


