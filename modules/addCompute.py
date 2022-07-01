from utils.run_command import _run





def addCompute():
    print("A continuacion se procedera a agregar un nodo computo a Openstack")
    print('Desea continuar?')
    print('S-Si    -   N-No')
    answer = input().capitalize()


    
    """ Si la respuesta es si """
    if(answer == 'S'):
        print("Generando clave de conexion...")
        """ Intentemos ejecutar el comando """
        
        command = 'sudo microstack add-compute'
        execucion_code= _run(command=command)
        if(execucion_code.check_returncode == 0):
            """ En caso de funcionar bien el comando """            
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
