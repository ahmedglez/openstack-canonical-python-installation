import os
from sqlite3 import Time
import sys
import time
from utils.install_function import installation
from utils.update_system import update_system
from utils.microstack_init import microstack_init



print('')
print('')
print('         SCRIPT AUTOMATIZADO PARA LA INSTALACION DE OPENSTACK EN UBUNTU')
print('')
print('')
print('************************************************')
print('Asegurese primero de tener los permisos de sudo ')
print('************************************************')
print('')
print('')


""" ACTUALIZACION DE PAQUETES DE UBUNTU """
update_system();

""" INSTALACION DE GIT """
installation('Git', 'sudo apt-get install git')

""" INSTALACION DE SNAP """
installation('Snap', 'sudo apt install snapd');

""" INSTALACION DE MICROSTACK """
installation('Microstack', 'sudo snap install microstack --beta')

""" INICIALIZAR MICROSTACK """
microstack_init()


