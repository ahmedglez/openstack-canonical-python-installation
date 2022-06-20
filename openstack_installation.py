import subprocess

""" 1. Actualizar Ubuntu """
subprocess.run(["sudo", "apt-get", "update"]);

""" 2. Instalar Python """
subprocess.run(["sudo","apt-get", "install", "pyhton"]);

""" 3. Instalar Git """
subprocess.run(["sudo","apt-get", "install", "git"]);

""" 4. Instalar snap """
subprocess.run(["sudo","apt", "update"]);
subprocess.run(["sudo","apt-get", "install", "snap"]);

""" 5. Probar snap """
subprocess.run(["sudo","snap", "install", "hello-world"]);
subprocess.run(["hello-world"]);

""" 6. Instalar microstack """
subprocess.run(["sudo","snap", "install", "microstack", "--beta"]);

""" 7.  Verificar que se instalo correctamente """
subprocess.run(["snap","list","microstack"]);

""" 8.  Inicializar microstack """
subprocess.run(["sudo", "microstack", "init", "--auto", "--control"]);











