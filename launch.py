### Pas encore Adapté des boxes

print("Demarrage 'launch.py'")
path = "C:/Users/Rezal/Documents/GitHub/WallStreetKfet/"

import time
import mysql.connector
from datetime import datetime
import pickle

exec(open(path+'QUERRY.py').read())
exec(open(path+'WallStreetConfig.py').read())
exec(open(path+'SQL.py').read())
# time.sleep(1)
# exec(open(path+'WallofGraphes.py').read())
exec(open(path+'WallStreetMode.py').read())
