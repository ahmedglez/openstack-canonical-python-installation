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
                addCompute()
    else:
        print('Respuesta no valida')
        addCompute()
