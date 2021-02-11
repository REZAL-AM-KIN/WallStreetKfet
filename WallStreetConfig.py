#Ici se trouvent les paramètres de bases à configurer avant la soirée et qui servent de bases

time_period = 1 #mins. ATTENTION <=30 sinon programme marche pas !! Correspond à l'interval d'actualisation des prix.
time_period_second = time_period * 60
isRunning = False # Active ou non le mode WallStreet.
previous_state = False # Comparé à la variable "isRunning", permet de constater un changement d'état marche/arrêt du jeu.
coef_lingus = 0.5 #Coeff de Lingus, scientifique connu du 21eme
produits_standard = [] #id et prix standards kfet
id_produit_jeu = [69, 2503, 4280, 4759] # ID des produits concernés par le jeu.

SQLid_produit_jeu = '(' + str(id_produit_jeu[0])# ID des pdts mais à utiliser pour les requetes
for i in id_produit_jeu[1:]:
    SQLid_produit_jeu += (', '+str(i))
SQLid_produit_jeu += (')')

# connection={}
# connection["user"]='*****'
# connection["password"]='********'
# connection["database"]='localhost'
# connection["host"]='GestionKINTest.db'

user = 'WallStreet'
password = '**'
database = 'GestionKIN'
host = '172.20.219.7'
