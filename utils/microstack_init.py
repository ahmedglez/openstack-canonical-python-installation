import os

def microstack_init():   
    print("A continuacion se procedera a inicializar Microstack en sus sistema operativo");
    print('Desea continuar?')
    print('S-Si    -   N-No')
    answer = input().capitalize()
    if(answer == 'S'):
        print("Inicializando Microsttack ...")
        output = os.system(" sudo microstack init --auto --control ")
    if(output != 0):
        print("")
        print("")
        print("Ha ocurrido un error en la instalacion")
        print(
            "Por favor compruebe su conexion y los permisos de usuario e intentelo de nuevo")
    elif(output == 1):
        print("Microstack inicializado con exito")