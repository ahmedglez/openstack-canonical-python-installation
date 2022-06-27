import os


def addCompute():
    print("A continuacion se procedera a agregar un nodo computo a Openstack")
    print('Desea continuar?')
    print('S-Si    -   N-No')
    answer = input().capitalize()
    if(answer == 'S'):
        print("Generando clave de conexion...")
        os.system('sudo microstack add-compute')
        print('')
        print('Ejecute el siguiente comando en la maquina designada como nodo de computo:')
        print('')
        print('sudo microstack init --auto --compute --join <clave de conexion>')
        print('')
        print('La clave de conexion solo es valida por 20 minutos')
        print("Nota: Cada nodo de cómputo adicional requerirá que se genere una nueva clave \n de conexión. Agregue tantos nodos de cómputo como desee repitiendo el proceso de \n combinación. El proceso de inicializacion en el nodo de computo es mucho mas rapido \n que en el nodo controlador. ")
