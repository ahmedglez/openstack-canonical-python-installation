

import os
import time


def update_system():
    print('A continuacion se procedera a actualizar los paquetes del sistema ')
    print('Desea continuar?')
    confirm1();


def confirm1():
    print('S-Si    -   N-No')
    answer = 0
    while(answer != 'S' and answer != 'N'):
        answer = input().capitalize()
        if(answer == 'S'):
            print("Actualizando paquetes del sistema...")
            output = os.system('sudo apt-get update')
            if(output != 0):
                print("")
                print("")
                print(
                    "Ha ocurrido un error intentando actualizar los paquetes del sistema")
                print("Por favor compruebe su conexion y los permisos de usuario")
                print(" ")
                print(" ")
                print("Desea reintentar desde el paso anterior?")
                print('S-Si    -   N-No')
                answer = input().capitalize()
                if(answer == 'S'):
                    confirm1()
                if(answer == 'N'):
                    break
            elif(output == 1):
                 print("Paquetes actualizados con exito!!")
        elif(answer == 'N'):
            answer2 = 0
            while(answer2 != 'S' and answer2 != 'N'):
                print("Desea omitir este paso?")
                print("S-Si        -       N-No")
                answer2 = input().capitalize();
                if(answer2 == 'S'):
                    break
                elif(answer2 == 'N'):
                     update_system()

        else:
            print('Opcion no valida')
       
