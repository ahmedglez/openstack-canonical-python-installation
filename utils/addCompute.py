import subprocess




def addCompute():
    print("A continuacion se procedera a agregar un nodo computo a Openstack")
    print('Desea continuar?')
    print('S-Si    -   N-No')
    answer = input().capitalize()


    
    """ Si la respuesta es si """
    if(answer == 'S'):
        print("Generando clave de conexion...")
        """ Intentemos ejecutar el comando """
        try:
            output = subprocess.check_output(
                'sudo microstack add-compute', stderr=subprocess.STDOUT, shell=True, timeout=3,
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
                    addCompute()
                elif(answer=='N'):
                    break
                else:
                    print('Opcion no valida')
        except subprocess.TimeoutExpired as exc:
            print("La ejecucion de este comando está demorado demasiado tiempo")
            print("Desea continuar con la ejecucion?")
            print('S-Si    -   N-No')
            answer = 0
            while(answer != 'S' and answer != 'N'):
                answer = input().capitalize()
                if(answer == 'S'):
                    print("Añadiendo nodo... ")
                elif(answer == 'N'):
                    break
                else:
                    print('Opcion no valida')

        else:
            """ En caso de funcionar bien el comando """
            print("Output: \n{}\n".format(output))
            print('')
            print(
                'Ejecute el siguiente comando en la maquina designada como nodo de computo:')
            print('')
            print('sudo microstack init --auto --compute --join <clave de conexion>')
            print('')
            print('La clave de conexion solo es valida por 20 minutos')
            print("Nota: Cada nodo de cómputo adicional requerirá que se genere una nueva clave \n de conexión. Agregue tantos nodos de cómputo como desee repitiendo el proceso de \n combinación. El proceso de inicializacion en el nodo de computo es mucho mas rapido \n que en el nodo controlador. ")
    elif(answer == 'N'):
        answer2 = 0
        while(answer2 != 'S' and answer2 != 'N'):
            print("Desea omitir este paso?")
            print("S-Si        -       N-No")
            answer2 = input().capitalize()
            if(answer2 == 'S'):
                break
            elif(answer2 == 'N'):
                addCompute()
    else:
        print('Respuesta no valida')
        addCompute()
