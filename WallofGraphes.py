from flask import Flask, render_template

# A retirer; pour test
import time
import mysql.connector
path = "C:/Users/Rezal/Documents/GitHub/WallStreetKfet/"
exec(open(path+'QUERRY.py').read())
exec(open(path+'WallStreetConfig.py').read())
exec(open(path+'SQL.py').read())


conso, prix = [], []
name_prix_produits = SQL_SELECT(QUERRY_getIdPrixProduits())

# hearder = ["Heure"]
# for produit in name_prix_produits:
# 	hearder.append(produit['name'])
# conso.append(header)
# prix.append(header)
# ------------------
# application Flask
# ------------------

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template("WallofGraphes.html", prix=prix, conso=conso);

# ---------------------------------------
# pour lancer le serveur web local Flask
# ---------------------------------------

if __name__ == '__main__':
    app.run(debug=True, port=5678)
