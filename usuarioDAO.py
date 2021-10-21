from usuario import Usuario
from conexion import Conexion
from logger_base import log
from cursor_pool import CursorDelPool
class UsuarioDAO:
    """
    DAO (Data Acces Object)
    CRUD (Create Read Update Delete )
    """
    
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_user'
    _INSERTAR = 'INSERT INTO usuario(user_name , user_password) VALUES(%s,%s)'
    _ACTUALIZAR = 'UPDATE usuario SET user_name = %s, user_password = %s WHERE id_user = %s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_user = %s'

    @classmethod
    def seleccionar(cls):
        
        with CursorDelPool() as cursor:
            
            cursor.execute(cls._SELECCIONAR) # no se pasa ningun placeholder 
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                # Creamos objetos de tipos Persona(le pso como prametros la info del "registro")
                persona = Usuario(registro[0],registro[1],registro[2])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls,persona):
        
        with CursorDelPool() as cursor:
            
            valores = (persona.user_name , persona.user_password)
            cursor.execute(cls._INSERTAR , valores)
            log.debug(f'Persona a insertar: {persona}')
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.user_name , persona.user_password ,  persona.id_user )
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Actualizacion del registro: {persona}')
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_user,) # es necesario que sea tupla
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Registro eliminado: {persona}')
            return cursor.rowcount
                
#-----------------------------TESTEO----------------------------- 

if __name__ == '__main__':
    print("SELECCIONAR ACCION:\n1: Pedir Registros\n2: Agregar registros\n3: Actualizar Registros\n4: Eliminar Registro")
    accion = int(input("-> "))
    
    # Seleccionar los registros
    if accion == 1:    
        persona = UsuarioDAO.seleccionar()
        for personas in persona:
            log.debug(personas)

    # Insertar registro
    if accion == 2:    
        persona1 = Usuario( user_name= "ApePrueb" , user_password= "0985")
        resultado = UsuarioDAO.insertar(persona1)
        log.debug(f"Registros insertados: {resultado}")

    # Actualizar registro:
    if accion == 3:
        persona1 = Usuario(1, "Jonatan Gabriel" , "0985")
        resultado = UsuarioDAO.actualizar(persona1)
        log.debug(f"Registros actualizaos: {resultado}")

    # Eliminar registro
    if accion == 4:
        persona1 = Usuario(id_user= 17)
        resultado = UsuarioDAO.eliminar(persona1)
        log.debug(f"Registros eliminados: {resultado}")

  


    

    