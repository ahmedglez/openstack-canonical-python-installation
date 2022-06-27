

import os
import time


def update_system():

    print('A continuacion se procedera a actualizar los paquetes del sistema ')
    print('Desea continuar?')
    print('S-Si    -   N-No')
    answer = input().capitalize()
    if(answer == 'S'):
        initial_time = time.localtime()
        print("Actualizando paquetes del sistema...")
        output = os.system('sudo apt-get update')
    if(output != 0):
        print("")
        print("")
        print("Ha ocurrido un error intentando actualizar los paquetes del sistema")
        print("Por favor compruebe su conexion y los permisos de usuario")
    elif(output == 1):
        print("Paquetes actualizados con exito!!")
