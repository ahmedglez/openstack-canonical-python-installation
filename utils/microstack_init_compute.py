import os

def microstack_init():   
    print("A continuacion se procedera a inicializar Microstack en su nodo de computo");
    print('Desea continuar?')
    print('S-Si    -   N-No')
    answer = input().capitalize()
    if(answer == 'S'):
        print("Inicializando Microstack ...")
        print("Escriba su clave de conexion")
        clave = input()
        print('Inicializacndo Openstack en su nodo computo')
        output = os.system(" sudo microstack init --auto --compute --join" + clave)
    elif(output != 0):
        print("")
        print("")
        print("Ha ocurrido un error en la inicializacion")
        print(
            "Por favor compruebe su conexion y los permisos de usuario e intentelo de nuevo")
        print("")       
        answer3=0;
        while(answer3 !='S' and answer3!='N'):
             print("Desea reintentar este paso nuevamente?")
             answer3 = input().capitalize()
             if(answer3 == 'S'):
                microstack_init();
             elif(answer3 == 'N'):
               return 0;
    elif(output == 1):
        print("Microstack inicializado con exito")