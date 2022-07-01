from modules.install_function import installation
from modules.update_system import update_system
from modules.microstack_init import microstack_init
from modules.addCompute import addCompute
from modules.microstack_init import microstack_init_compute
import os


os.system('clear')
print('')
print('')
print('         SCRIPT AUTOMATIZADO PARA LA INSTALACION DE OPENSTACK CANONICAL EN UBUNTU')
print('')
print('')
print('************************************************')
print('Asegurese primero de tener los permisos de sudo ')
print('************************************************')
print('')
print('')

""" ACTUALIZACION DE PAQUETES DE UBUNTU """
print('***Paso#1 - Actualizacion de los paquetes del sistema operativo***')
update_system();
print("")

""" INSTALACION DE GIT """
print('***Paso#2 - Instalacion de Git***')
installation('Git', 'sudo apt-get install git')
print("")


""" INSTALACION DE SNAP """
print('***Paso#3 - Instalacion de Snap***')
installation('Snap', 'sudo apt install snapd');
print("")


""" INSTALACION DE MICROSTACK """
print('***Paso#4 - Instalacion de Microstack***')
installation('Microstack', 'sudo snap install microstack --beta')
print("")


""" INICIALIZAR MICROSTACK """
print('***Paso#5 - Inicializacion de nodo computo de Openstack*** ')
microstack_init('computo', 'sudo microstack init --auto --compute --join' );
print("")

