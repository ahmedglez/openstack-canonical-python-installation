import subprocess
import os;


def microstack_init():    
    print("A continuacion se procedera a inicializar Microstack en su nodo controlador")
    print('Desea continuar?')
    print('S-Si    -   N-No')
    answer = input().capitalize()

    if(answer == 'S'):
        print("Inicializando Microstack en su nodo controlador ...")
        os.system('sudo snap abort --last=install')
        try:
            command = 'sudo microstack init --auto --control '
            output = subprocess.check_output(
                command, stderr=subprocess.STDOUT, shell=True, timeout=50,
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
                    microstack_init()
                elif(answer == 'N'):
                    break
                else:
                    print('Opcion no valida')
        except subprocess.TimeoutExpired as exc:
                print("")
                print("La ejecucion de este comando está demorado demasiado tiempo")
                print("Desea reintentar este paso?")
                print('S-Si    -   N-No')
                answer = 0
                while(answer != 'S' and answer != 'N'):
                    answer = input().capitalize()
                    if(answer == 'S'):
                        microstack_init()

                    elif(answer == 'N'):
                        print(subprocess.check_output())
                    else:
                        print('Opcion no valida')

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
                microstack_init()

    else:
        """ Ninguna de las opciones """
        print('Opcion no valida')
        microstack_init()
