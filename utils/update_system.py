

from asyncio import wait
from utils.run_command import _run
import subprocess


def update_system():
    print('A continuacion se procedera a actualizar los paquetes del sistema ')
    print('Desea continuar?')
    confirm1()


def confirm1():
    print('S-Si    -   N-No')
    answer = 0
    while(answer != 'S' and answer != 'N'):
        answer = input().capitalize()
        if(answer == 'S'):
            print("Actualizando paquetes del sistema...")
            
            command = 'sudo apt-get update '
            _run(command=command)

        elif(answer == 'N'):
            answer2 = 0
            while(answer2 != 'S' and answer2 != 'N'):
                print("Desea omitir este paso?")
                print("S-Si        -       N-No")
                answer2 = input().capitalize()
                if(answer2 == 'S'):
                    break
                elif(answer2 == 'N'):
                    update_system()

        else:
            print('Opcion no valida')
