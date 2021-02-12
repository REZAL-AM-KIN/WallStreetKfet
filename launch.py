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
exec(open(path+'WallStreetMode.py').read())
