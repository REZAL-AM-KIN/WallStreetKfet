from flask import Flask, render_template
import pickle

# ------------------
# application Flask
# ------------------

with open("name_produit.txt", "rb") as fp: 
		name_produit = pickle.load(fp)

app = Flask(__name__)

@app.route("/")
def index():
	with open("all_prix.txt", "rb") as fp: 
		all_prix = pickle.load(fp)
	with open("all_lccp.txt", "rb") as fp:   
		all_lccp = pickle.load(fp)
	tableau_prix = [["Période"]+name_produit]
	tableau_conso = [["Période"]+name_produit]
	for i in range(0,len(all_prix)):
		conso, prix = [],  []
		for j in range(0,len(name_produit)):
			print(j)
			conso.append(all_lccp[i][j])
			prix.append(all_prix[i][j])
		tableau_conso.append([i]+conso)
		tableau_prix.append([i]+prix)

	return render_template("WallofGraphes.html", prix=tableau_prix, conso=tableau_conso);

# ---------------------------------------
# pour lancer le serveur web local Flask
# ---------------------------------------

if __name__ == '__main__':
    app.run(debug=True, port=5678)
