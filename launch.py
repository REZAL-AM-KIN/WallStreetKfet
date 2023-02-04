### Pas encore Adapté des boxes

print("Demarrage 'launch.py'")
path = "/home/rezal/WallStreetKfet/"

import time
import mysql.connector
from datetime import datetime
import pickle
import subprocess

exec(open(path+'QUERRY.py').read())
exec(open(path+'WallStreetConfig.py').read())
exec(open(path+'SQL.py').read())
# time.sleep(1)
#exec(open(path+'WallofGraphes.py').read())
#subprocess.call('start /wait python WallofGraphes.py', shell=True)

# Launch the Flask server
# launch the main loop

Nb_de_Periodes = int(input("\nCombien de manches de '{0}' minutes voulez vous jouer ?\nAttention ! La partie ne peut être arrêtée en cours et les prix norm'sss kfet seront automatiquement remis à la fin. : \n".format(time_period)))
print("Le mode WallStreet sera actif pendant '{0}' minutes. NE PAS ETEINDRE LA VM pendant (sinon faudra rechanger les prix modifiés à la main ...)".format(time_period * Nb_de_Periodes))


exec(open('/home/justin/Dev_n_Class/WallStreetKfet/WallStreetMode.py').read())
