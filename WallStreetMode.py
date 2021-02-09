#Ici c'est le coeur du truc, qui va tourner en fond et gérer la soirée


import WallStreetConfig.py

isRunning = True

def CalculPrix():
    C_j = []
    C_j_moins_un = []
    M_kfet = 0
    M_P3 = 0

    for produit in id_produit_jeu: #pour tous les produits
        query = f"SELECT produits_id FROM consos WHERE date>{unix_time-time_period_second} AND produits_id={produit["id"]}"
        conso_j = SQL_SELECT(query) #Consommation des produits concernés sur la période
        query = f"SELECT produits_id FROM consos WHERE date<={unix_time-time_period_second} AND date>{unix_time-2*time_period_second} AND produits_id={produit["id"]}"
        conso_j_moins_un = SQL_SELECT(query)

        id_produit = str(produit["id"])

        C_j[id_produit] = len(conso_j)
        C_j_moins_un[id_produit] = len(conso_j_moins_un)

        M_kfet += marge_kfet*C_j[id_produit]*prix_kfet[id_produit]
        M_P3 += (prix_P3[id_produit]-prix_kfet[id_produit])*c_j[id_produit]

    A = M_kfet - M_P3

    prix_P3_futur = {}
    for produit in produit_standard:
        id_produit = str(produit["id"])

        x = A / c_j[id_produit]

        if c_j[id_produit] >= C_j_moins_un[id_produit]: #Check formule
            prix_P3_futur[id_produit] = prix_kfet[id_produit]*(1+(C_j_moins_un[id_produit]/sum(C_j_moins_un.values())))*coef_lingus + x
        else:
            prix_P3_futur[id_produit] = prix_kfet[id_produit]*(1-(C_j_moins_un[id_produit]/sum(C_j_moins_un.values())))*coef_lingus + x



while True:
    if isRunning != previous_state: #permet de constater que le jeu démarre ou s'arrête

        if isRunning: # si c'est un demarrage, on stock les bons prix
            prix_kfet = {}
            for produit in produit_standard:
                prix_kfet[str(produit["id"])]=produit["prix"]
            previous_state = isRunning

        else: #Si c'est un arret, on remet les bons prix
            for p in produit_standard:
                SQL_UPDATE(QUERRY_setMontant(p["id"],p["prix"]))
            previous_state = isRunning

    elif isRunning: #On a deja demarré et on est en jeu

    ### 1ère étape: Connection à la bdd & SELECT de produit et compte sur la période.
        produits = SQL_SELECT(QUERRY_getConsoPeriode())

    ### 2ème étape: Calcul des nouveaux prix à partir des formules de Lingus.
        prix_P3_produit_jeu = CalculPrix()

	### 3ème étape: UPDATE des prix kfet dans la bdd
        for i in range (len(prix_P3_produit_jeu)) :
            SQL_UPDATE(QUERRY_setMontant(id_produit_jeu[i], prix_P3_produit_jeu[i]))

    else: # On a arrété le jeu et tout est remis en place, on quitte
        break

    sleep(time_period_second)
