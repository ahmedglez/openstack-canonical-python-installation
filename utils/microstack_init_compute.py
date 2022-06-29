import subprocess;

def microstack_init():   
    print("A continuacion se procedera a inicializar Microstack en su nodo de computo");
    print('Desea continuar?')
    print('S-Si    -   N-No')
    answer = input().capitalize()


    if(answer == 'S'):
        print("Escriba su clave de conexion")
        clave = input()
        print('Inicializacndo Openstack en su nodo computo')
               
        try:
            command = 'sudo microstack init --auto --compute --join '+clave
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
                    microstack_init()
                elif(answer=='N'):
                    break
                else:
                    print('Opcion no valida')
        except subprocess.TimeoutExpired as exc:             
            print("Error, Status : FAIL", exc.returncode, exc.output)
            print("La ejecucion de este comando ha demorado demasiado tiempo")
            print("Desea reintentar este paso nuevamente?")
            print('S-Si    -   N-No')
            answer = 0
            while(answer != 'S' and answer != 'N'):
                answer = input().capitalize()
                if(answer == 'S'):
                    microstack_init()
                elif(answer=='N'):
                    break
                else:
                    print('Opcion no valida')
    

    elif(answer == 'N'):
        """ En caso de No """
        answer2 = 0;
        while(answer2 != 'S' and answer2 != 'N'):
            print("Desea omitir este paso?")
            print("S-Si        -       N-No")
            answer2 = input().capitalize();
            if(answer2 == 'S'):
                break
            elif(answer2 == 'N'):
                microstack_init()

                
    else:
        """ Ninguna de las opciones """
        print('Opcion no valida')
        microstack_init()
