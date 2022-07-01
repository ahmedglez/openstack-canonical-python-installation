from utils.run_command import _run


def microstack_init_compute(name, command):   
    print("A continuacion se procedera a inicializar Microstack en su nodo de computo");
    print('Desea continuar?')
    print('S-Si    -   N-No')
    answer = input().capitalize()


    if(answer == 'S'):
        if(name=='computo'):
            print("Escriba su clave de conexion")
            clave = input()
            command = command + " "+ clave

        print('Inicializacndo Openstack en su nodo '+name) 
        ex_result = _run(command=command)
        if(ex_result == 1):
            """ En caso de error """
            print("Error, Status : FAIL", ex_result.returncode, ex_result.output)
            print("")
            print("Desea reintentar este paso nuevamente?")
            print('S-Si    -   N-No')
            answer = 0
            while(answer != 'S' and answer != 'N'):
                answer = input().capitalize()
                if(answer == 'S'):
                    microstack_init_compute()
                elif(answer=='N'):
                    break
                else:
                    print('Opcion no valida')

        else:
            print("")
            print("Microstack inicializado correctamente en su nodo "+name)

    

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
