from usuario import Usuario
from usuarioDAO import UsuarioDAO
from logger_base import log

print("CONSOLA DE BASE DE DATOS".center(50,"-"))
accion = None
name = None
contra = None
id_ = None


while accion != 5:

    print("\nSELECCIONAR ACCION:\n1: Pedir Registros\n2: Agregar registros\n3: Actualizar Registros\n4: Eliminar Registro\n5: Salir")
    accion = int(input("-> "))

    # Seleccionar los registros
    if accion == 1:    
        persona = UsuarioDAO.seleccionar()
        for personas in persona:
            print("\n")
            log.debug(personas)

    # Insertar registro
    if accion == 2:
        name = input("\nIngresar NOMBRE DE USUARIO: ")
        contra = input("Ingresar CONTRASEÑA: ")    
        persona1 = Usuario(user_name= name, user_password = contra )
        resultado = UsuarioDAO.insertar(persona1)
        log.debug(f"Registros insertados: {resultado}")

    # Actualizar registro:
    if accion == 3:
        id_ = int(input("\nIngresar ID a actualizar: "))
        name = input("Ingresar nuevo NOMBRE DE USUARIO: ")
        contra = input("Ingresar nuevo CONTRASEÑA: ")    

        persona1 = Usuario(id_ , name , contra)
        resultado = UsuarioDAO.actualizar(persona1)
        log.debug(f"Registros actualizaos: {resultado}")

    # Eliminar registro
    if accion == 4:
        id_ = int(input("Ingresar ID a eliminar: "))
        persona1 = Usuario(id_user= id_)
        resultado = UsuarioDAO.eliminar(persona1)
        log.debug(f"Registros eliminados: {resultado}")