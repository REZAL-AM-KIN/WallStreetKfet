#Ici se trouvent les paramètres de bases à configurer avant la soirée et qui servent de bases

time_period = 1 #mins. ATTENTION <=30 et >=1 sinon programme marche pas !! Correspond à l'interval d'actualisation des prix.
time_period_second = time_period * 60
isRunning = False # Active ou non le mode WallStreet.
previous_state = False # Comparé à la variable "isRunning", permet de constater un changement d'état marche/arrêt du jeu.
coef_lingus = 0.3 #Coeff de Lingus, scientifique connu du 21eme
produits_standard = [] #id et prix standards kfet
id_produit_jeu = [4973, 4974, 4975, 4976, 4977, 4978, 4979, 4980, 4981, 4982, 4983, 4984, 4985, 4986] # ID des produits concernés par le jeu.
Nb_de_Periodes = int(input("\nCombien de manches de '{0}' minutes voulez vous jouer ?\nAttention ! La partie ne peut être arrêtée en cours et les prix norm'sss kfet seront automatiquement remis à la fin. : \n".format(time_period)))
print("Le mode WallStreet sera actif pendant '{0}' minutes. NE PAS ETEINDRE LA VM pendant (sinon faudra rechanger les prix modifiés à la main ...)".format(time_period * Nb_de_Periodes))
SQLid_produit_jeu = '(' + str(id_produit_jeu[0])# ID des pdts mais à utiliser pour les requetes
for i in id_produit_jeu[1:]:
    SQLid_produit_jeu += (', '+str(i))
SQLid_produit_jeu += (')')
name_produit = []
all_Lccp, all_prix = [], []

# connection={}
# connection["user"]='*****'
# connection["password"]='********'
# connection["database"]='localhost'
# connection["host"]='GestionKINTest.db'

user = 'WallStreet'
password = '**'
database = 'GestionKIN'
host = '172.20.219.7'
