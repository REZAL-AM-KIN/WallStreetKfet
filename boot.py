### Pas encore Adapté des boxes

print("Demarrage 'boot.py'")
path = '/Users/Nathan/Documents/GitHub/WallStreetKfet/'

import time
import mysql.connector
from datetime import datetime

exec(open(path+'QUERRY.py').read())
exec(open(path+'WallStreetConfig.py').read())
exec(open(path+'SQL.py').read())
exec(open(path+'WallStreetMode.py').read())
exec(open(path+'WallofGraphes.py').read())
