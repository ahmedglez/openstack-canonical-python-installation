

import subprocess
import time


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
            try:
                command = 'sudo apt-get update '
                output = subprocess.check_output(
                    command, stderr=subprocess.STDOUT, shell=True, timeout=3,
                    universal_newlines=True)
            except subprocess.CalledProcessError as exc:
                """ En caso de error """
                print("Error, Status : FAIL", exc.returncode, exc.output)
                print("")
                print("Desea reintentar este paso nuevamente?")
                print('S-Si    -   N-No')
                answer = 0
                while(answer != 'S' and answer != 'N'):
                    answer = input().capitalize()
                    if(answer == 'S'):
                        update_system()
                    elif(answer == 'N'):
                        break
                    else:
                        print('Opcion no valida. Intentelo de nuevo')
            except subprocess.TimeoutExpired as exc:             
                print("Error, Status : FAIL", exc.returncode, exc.output)
                print("La ejecucion de este comando ha demorado demasiado tiempo")
                print("Desea reintentar este paso nuevamente?")
                print('S-Si    -   N-No')
                answer = 0
                while(answer != 'S' and answer != 'N'):
                    answer = input().capitalize()
                    if(answer == 'S'):
                        update_system()
                    elif(answer=='N'):
                        break
                    else:
                        print('Opcion no valida')

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
