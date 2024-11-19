usuarios = {
    "usuario1": "contraseña1",
    "usuario2": "contraseña2"
}

def iniciar_sesion():
    print("\n\t╔═════════════════════════════╗")
    print("\t║       Iniciar Sesión        ║")
    print("\t╚═════════════════════════════╝\n")

    usuarioLogeado = True

    while usuarioLogeado == False:

        usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        if usuario in usuarios:
            if usuarios[usuario] == contrasena:
                print("\n\t╔═════════════════════════════╗")
                print("\t║  Inicio de sesión exitoso!  ║")
                print("\t╚═════════════════════════════╝\n")
                usuarioLogeado = True
            else:
                print("\n\t╔═════════════════════════════╗")
                print("\t║   Contraseña incorrecta.    ║")
                print("\t╚═════════════════════════════╝\n")
        else:
            print("\n\t╔═════════════════════════════╗")
            print("\t║  Usuario no encontrado.     ║")
            print("\t╚═════════════════════════════╝\n")

