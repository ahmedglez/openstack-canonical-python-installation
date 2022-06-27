import os;

def installation(name, command):
    print("")
    print("")
    print("A continuacion se procedera a instalar " +
          name + " en sus sistema operativo")
    print('Desea continuar?')
    print('S-Si    -   N-No')
    answer = input().capitalize()
    if(answer == 'S'):
        print("Instalando Git en su sistema operativo ...")
        output = os.system(command)
    if(output != 0):
        print("")
        print("")
        print("Ha ocurrido un error en la instalacion")
        print(
            "Por favor compruebe su conexion y los permisos de usuario e intentelo de nuevo")
    elif(output == 1):
        print("Instalacion concluida con exito")