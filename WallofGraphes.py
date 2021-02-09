from flask import Flask, render_template
import mysql.connector
import SQL.py
import QUERRY.py
from WallStreetConfig.py import *
import time

def SQL_SELECT(querry, con):
    _cnx=mysql.connector.connect(con)
    _cursor=_cnx.cursor()
    _cursor.execute(querry)
    _select=_cursor.fetchall()
    _cnx.close()
    return _select

def QUERRY_getIdPrixProduits(ids):
    return (f"SELECT name, id, prix FROM produits WHERE id IN {id_produit_jeu} ;")

def QUERRY_getConsoPeriode(IDproduit): #renvoie le nb vendu sur la periode pour UN PRODUIT
    return (f"SELECT count(*) FROM consos WHERE produits_id = {IDproduit} AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < {'00:'+str(time_period)+':00'} ;")

conso, prix = [], []
name_prix_produits = SQL_SELECT(QUERRY_getIdPrixProduits(id_produit_jeu))

hearder = ["Heure"]
for produit in name_prix_produits:
	hearder.append(produit['name'])
conso.append(header)
prix.append(header)
# ------------------
# application Flask
# ------------------

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template("WallofGraphes.html", prix=prix, conso=conso);
	name_prix_produits = SQL_SELECT(QUERRY_getIdPrixProduits(id_produit_jeu))
	now = datetime.datetime.now() # Une requête pour avoir le temps SQL serait bien
	heure = str(now.hour)+":"+str(now.min)
	new_conso = [heure]
	new_prix = [heure]
	for produit in name_prix_produits:
	    new_prix.append(produit['prix'])
	    new_conso.append(SQL_SELECT(QUERRY_getConsoPeriode(produit['id'])))
	prix.append(new_prix)
	conso.append(new_conso)
    


# ---------------------------------------
# pour lancer le serveur web local Flask
# ---------------------------------------

if __name__ == '__main__':
    app.run(debug=True, port=5678)
