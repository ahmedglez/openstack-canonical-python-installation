from multiprocessing.connection import wait
from utils.run_command import _run
import os



def installation(name, command):

    print("A continuacion se procedera a instalar " +
          name + " en sus sistema operativo")
    print('Desea continuar?')
    print('S-Si    -   N-No')
    answer = input().capitalize()

    if(answer == 'S'):
        """ En caso de elegir Si """
        print("Instalando " + name + " en su sistema operativo ...")
        _run(command=command)
        



    elif(answer == 'N'):
        """ En caso de No """
        answer2 = 0
        while(answer2 != 'S' and answer2 != 'N'):
            print("Desea omitir este paso?")
            print("S-Si        -       N-No")
            answer2 = input().capitalize()
            if(answer2 == 'S'):
                break
            elif(answer2 == 'N'):
                installation(name, command)

    else:
        """ Ninguna de las opciones """
        print('Opcion no valida')
        installation(name, command)
