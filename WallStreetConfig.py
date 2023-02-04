#Ici se trouvent les paramètres de bases à configurer avant la soirée et qui servent de bases


#mins. ATTENTION <=30 et >=1 sinon programme marche pas !! Correspond à l'interval d'actualisation des prix.
time_period = 1
time_period_second = time_period * 60

# Nb_de_Periodes = // à entrer par l'utilisateur

# Active ou non le mode WallStreet.
isRunning = False

# Comparé à la variable "isRunning", permet de constater un changement d'état marche/arrêt du jeu.
previous_state = False

# Coeff de Lingus, scientifique connu du 21eme
coef_lingus = 0.3

# id et prix standards kfet
produits_standard = []

# ID des produits concernés par le jeu.
id_produit_jeu = [4973, 4974, 4975, 4976, 4977, 4978, 4979, 4980, 4981, 4982, 4983, 4984, 4985, 4986]

# ID des pdts mais à utiliser pour les requetes
SQLid_produit_jeu = '(' + str(id_produit_jeu[0])
for i in id_produit_jeu[1:]:
    SQLid_produit_jeu += (', '+str(i))
SQLid_produit_jeu += (')')
name_produit = []
all_Lccp, all_prix = [], []


# DB credentials
user = 'WallStreet'
password = 'DumbPassword'
database = 'GestionKIN'
host = '172.20.76.30'
