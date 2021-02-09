"""
Brouillon de WallStreet K'fet usiné par Iz'Or 165tt KIN218, sur les calculs pistons de Lingus 99µ4 KIN218, supervisé par Hawking 172µ108 KIN218.
"""
### IMPORT ###
# import time
# import mysql
# import SQL.py # github rezalkin>piconflex2000-fonctions>SQL, modifier lien BDD
#
# ### VARIABLE ###
# time_period = 30 #mins. Correspond à l'interval d'actualisation des prix.
# time_period_second = time_period * 60
# is_it_running = False # Permet d'activé ou non l'update des prix en fonction de la consommation sur les "=time_period" minutes.
# previous_state = False # Comparé à la variable "is_it_running", permet de constater un changement d'état marche/arrêt du jeu.
# marge_kfet = 0.1 # Marge standard de la kfet
# coef_lingus = 0.5
# id_produit_jeu = (1, 2 ,3 ,4) # ID des produits concernés par le jeu.
#
#
# # Remplacez "While True" par une exécution du code toutes les "=time_period" minutes.
# While True:
# 	else:
# 	# Connection à la base de donnée
# 		if is_it_running != previous_state:
			## Cette condition permet de constaster un démarrage ou arrêt du jeu.
			## Pour l'instant, je stock les prix standards dans des variables, mais ce n'est pas très sûr en cas d'interruption du programme
			## pendant le jeu. Il faudrait préverer l'écriture/lecture sur un fichier.
			## L’idéal serait une fonction « EndGame » a laquelle on peut faire appel une fois terminé,
			## mais pour une première version ouais on va être obligé de faire ça.
			## if is_it_running:
			## 	### Sauvegarde les prix standards, il faudra les rememettre en place à la fin du jeu !
			# 	query = f"SELECT id, prix FROM produits WHERE id IN {id_produit_jeu}"
			# 	produit_standard = SQL_SELECT(query)

			# 	prix_kfet = {}
			# 	for produit in produit_standard:
			# 		prix_kfet[str(produit["id"])]=produit["prix"]
			#
			# 	previous_state = is_it_running
			# elif previous_state:
			# 	### J'utilise la sauvegarde des prix précédemment faite pour les remettre en place.
			# 	querrys = ""
			# 	for produit in produit_standard:
			# 		querrys += f"UPDATE produits SET prix={produit["prix"]} WHERE id={produit["id"]};"
			# 	SQL_UPDATE(querrys)
			#
			# 	previous_state = is_it_running
		# 
		#
		# if is_it_running:
		# 	# Le jeu tourne et nous somme sur une période d'actualisation
		# 	# Question: Peut-il avoir une intérerence entre l'actualisation des prix et le passage du commande simultanément ?
		# 	# Iz'Or: Je ne pense pas, grâce à la structure de SQL. Au pire, la commande ne sera pas prise en compte sur la bonne période de temps.
		#
		# 	### 1ère étape: Connection à la base de donnée & SELECT de consos, produit, prix depuis la bdd des produits concernés sur la bonne période.
		# 	query = f"SELECT id, prix FROM produits WHERE id IN {id_produit_jeu}"
		# 	produits = SQL_SELECT(query)
		# 	prix_P3 = {}
		# 	for produit in produits:
		# 		prix_P3[str(produit["id"])]=produit["prix"]
		#
		# 	### 2ème étape: Calcul des nouveaux prix à partir des formules de Lingus.
		# 	C_j = {}
		# 	C_j_moins_un = {}
		# 	M_kfet = 0
		# 	M_P3 = 0
		#
		# 	unix_time = time.time()
		# 	for produit in produit_standard:
		# 		query = f"SELECT produits_id FROM consos WHERE date>{unix_time-time_period_second} AND produits_id={produit["id"]}"
		# 		conso_j = SQL_SELECT(query) #Consommation des produits concernés sur la période
		# 		query = f"SELECT produits_id FROM consos WHERE date<={unix_time-time_period_second} AND date>{unix_time-2*time_period_second} AND produits_id={produit["id"]}"
		# 		conso_j_moins_un = SQL_SELECT(query)
		#
		# 		id_produit = str(produit["id"])
		#
		# 		C_j[id_produit] = len(conso_j)
		# 		C_j_moins_un[id_produit] = len(conso_j_moins_un)
		#
		# 		M_kfet += marge_kfet*C_j[id_produit]*prix_kfet[id_produit]
		# 		M_P3 += (prix_P3[id_produit]-prix_kfet[id_produit])*c_j[id_produit]
		#
		# 	A = M_kfet - M_P3
		#
		# 	prix_P3_futur = {}
		# 	for produit in produit_standard:
		# 		id_produit = str(produit["id"])
		#
		# 		x = A / c_j[id_produit]
		#
		# 		if c_j[id_produit] >= C_j_moins_un[id_produit]: #Check formule
		# 			prix_P3_futur[id_produit] = prix_kfet[id_produit]*(1+(C_j_moins_un[id_produit]/sum(C_j_moins_un.values())))*coef_lingus + x
		# 		else:
		# 			prix_P3_futur[id_produit] = prix_kfet[id_produit]*(1-(C_j_moins_un[id_produit]/sum(C_j_moins_un.values())))*coef_lingus + x
		#
		#
		# 	### 3ème étape: UPDATE des prix kfet dans la bdd.
		# 	querrys = ""
		# 	for produit in produit_standard:
		# 		id_produit = str(produit["id"])
		# 		query += f"UPDATE produits SET prix={prix_P3_futur[id_produit]} WHERE id={id_produit};"
		# 	SQL_UPDATE(querrys)

			### Optionnel 1: Sauvegarde des informations pour un éventuel check de négat's kfet.

			### optionnel 2: Sauvegarde dans une nouvelle table de la bdd de la variation des prix pour un futur affichage web.
