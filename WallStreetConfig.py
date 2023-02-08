#Ici se trouvent les paramètres de bases à configurer avant la soirée et qui servent de bases


#mins. ATTENTION <=30 et >=1 sinon programme marche pas !! Correspond à l'interval d'actualisation des prix.
# time_period = 2
# time_period_second = time_period * 60



REFRESH_INTERVAL = 1 * 60   # [s]; fréquence à laquelle les prix sont recalculés

# égale pour le modèle 220
PERIOD_SIZE = REFRESH_INTERVAL    # [s]; fenêtre de temps sur laquelle les consommations sont comptées

# Nb_de_Periodes = // à entrer par l'utilisateur

# Active ou non le mode WallStreet.
isRunning = False

# Comparé à la variable "isRunning", permet de constater un changement d'état marche/arrêt du jeu.
previous_state = False

# negat's P3 autorisé
NEGATS_P3 = 30

# Coef de Phik's,
# utile pour le modèle 220
COEF_PHIKS = 0.3

# Coeff de Lingus, scientifique connu du 21eme
# utile seulement pour le modèle 218
coef_lingus = 0.3

# id et prix standards kfet
produits_standard = []

# ID des produits concernés par le jeu.
id_produit_jeu = [4924, 5026, 4674, 4698]

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
