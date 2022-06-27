import os


def installation(name, command):
   
    print("A continuacion se procedera a instalar " +
          name + " en sus sistema operativo")
    print('Desea continuar?')
    print('S-Si    -   N-No')
    answer = input().capitalize()
    if(answer == 'S'):
        print("Instalando " +name+ " en su sistema operativo ...")
        output = os.system(command)
        if(output != 0):
            print("")
            print("")
            print("Ha ocurrido un error en la instalacion")
            print(
                "Por favor compruebe su conexion y los permisos de usuario e intentelo de nuevo")
        elif(output == 0):
            print("Instalacion concluida con exito")

    elif(answer == 'N'):
        answer2 = 0;
        while(answer2 != 'S' and answer2 != 'N'):
            print("Desea omitir este paso?")
            print("S-Si        -       N-No")
            answer2 = input().capitalize();
            if(answer2 == 'S'):
                break
            elif(answer2 == 'N'):
                installation(name,command)
    else:
        print('Opcion no valida')
    