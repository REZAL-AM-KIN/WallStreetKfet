#Ici se trouvent les paramètres de bases à configurer avant la soirée et qui servent de bases
import mysql.connector
import SQL.py
import QUERRY.py

time_period = 30 #mins. Correspond à l'interval d'actualisation des prix.
time_period_second = time_period * 60
isRunning = False # Active ou non le mode WallStreet.
previous_state = False # Comparé à la variable "isRunning", permet de constater un changement d'état marche/arrêt du jeu.
marge_kfet = 0.1 # Marge standard de la kfet
marge_p3 = 0.1
coef_lingus = 0.5
# prix_produit_jeu = []
# prix_P3_produit_jeu = []
prix_standard_biblio = {} #prix standards kfet
id_produit_jeu = (1, 2 ,3 ,4) # ID des produits concernés par le jeu.

connection={}
connection["user"]='*****'
connection["password"]='********'
connection["database"]='GestionKINTest'
connection["host"]='GestionKINTest.db'
