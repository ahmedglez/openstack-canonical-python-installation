import subprocess

""" 1. Actualizar Ubuntu """
subprocess.run(["echo","Actualizando Ubuntu ..."]);
output = subprocess.run(["sudo", "apt-get", "update"]);

""" 3. Instalar Git """
subprocess.run(["echo","Instalando Git ..."])
subprocess.run(["sudo","apt-get", "install", "git"]);

""" 4. Instalar snap """
subprocess.run(["echo","Instalando Snap ..."])
subprocess.run(["sudo","apt", "update"]);
subprocess.run(["sudo","apt-get", "install", "snap"]);

""" 5. Probar snap """
subprocess.run(["echo","Comprobando que snap funcione correctamente ..."])
subprocess.run(["sudo","snap", "install", "hello-world"]);
subprocess.run(["hello-world"]);

""" 6. Instalar microstack """
subprocess.run(["echo","Instalando Microstack ..."])
subprocess.run(["sudo","snap", "install", "microstack", "--beta"]);

""" 7.  Verificar que se instalo correctamente """
subprocess.run(["echo","Comprobando que Microstack se instaló correctamente ..."])
subprocess.run(["snap","list","microstack"]);

""" 8.  Inicializar microstack """
subprocess.run(["echo","Inicializando Microstack ..."])
subprocess.run(["sudo", "microstack", "init", "--auto", "--control"]);











