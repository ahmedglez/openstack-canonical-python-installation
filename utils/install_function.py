import subprocess
import os

""" import subprocess
try:
    output = subprocess.check_output(
        cmnd, stderr=subprocess.STDOUT, shell=True, timeout=3,
        universal_newlines=True)
except subprocess.CalledProcessError as exc:
    print("Status : FAIL", exc.returncode, exc.output)
else:
    print("Output: \n{}\n".format(output)) """


def installation(name, command):

    print("A continuacion se procedera a instalar " +
          name + " en sus sistema operativo")
    print('Desea continuar?')
    print('S-Si    -   N-No')
    answer = input().capitalize()

    if(answer == 'S'):
        """ En caso de elegir Si """

        print("Instalando " + name + " en su sistema operativo ...")

        try:
            output = subprocess.run(
                command, stderr=subprocess.STDOUT, shell=True, timeout=30,
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
                    if(name == 'Microstack'):
                        print('Eliminando procesos de snap en ejecucion')
                        os.system('sudo snap abort --last=install')
                        print("")
                        print("")
                        print("")
                        print("")
                        print("")
                        print("")
                        print("")
                    installation(name, command)
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
                        installation(name, command)

                    elif(answer == 'N'):
                        print(subprocess.check_output())
                    else:
                        print('Opcion no valida')

        else:
            print("")
            print(name, " ha sido correctamente instalado en su equipo")
            print("")
            print("")

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
