#Ici c'est le coeur du truc, qui va tourner en fond et gérer la soirée


import WallStreetConfig.py

isRunning = True

def CalculPrix(prix_standard_biblio):
    Conso_total_periode = SQL_SELECT(QUERRY_getConsoTotalePeriode())
    Prix_periode = SQL_SELECT(QUERRY_getIdPrixProduits())
    M_kfet, M_P3 = 0, 0
    Prix_periode_futur = []

    for produit in Prix_periode:
            Conso_produit_periode = SQL_SELECT(QUERRY_getConsoPeriode(produit['id']))
            Conso_produit_periode_biblio[produit['id']] = Conso_produit_periode # On sauvegarde dans une biblio pour ne pas refaire la même requête juste après
            M_kfet += marge_kfet*Conso_produit_periode*produit['prix']
            M_P3 += Conso_produit_periode*(produit['prix']-prix_standard_biblio[produit['id']])
    A = M_kfet - M_P3
    for produit in Prix_periode:
        x = A / Conso_produit_periode_biblio[produit['id']]
        Conso_produit_periode_precedente = SQL_SELECT(QUERRY_getConsoPeriodeMoinsUn(produit['id']))
        if Conso_produit_periode_biblio[produit['id']] >= Conso_produit_periode_precedente:
            Prix_periode_futur.append([produit['id'], prix_standard_biblio[produit['id']]*(1+(Conso_produit_periode_biblio[produit['id']]/Conso_total_periode))*coef_lingus + x ])
        else:
            Prix_periode_futur.append([produit['id'],prix_standard_biblio[produit['id']]*(1-(Conso_produit_periode_biblio[produit['id']]/Conso_total_periode))*coef_lingus + x ])
    return Prix_periode_futur


while True:
    if isRunning != previous_state: #permet de constater que le jeu démarre ou s'arrête

        if isRunning: # si c'est un demarrage, on stock les bons prix
            produits_standard = SQL_SELECT(QUERRY_getIdPrixProduits())
            for produit in produits_standard:
                prix_standard_biblio[produit['id']]=produit['prix']
            previous_state = isRunning

    elif isRunning: #On a deja demarré et on est en jeu

    ### 1ème étape: Calcul des nouveaux prix à partir des formules de Lingus.
        prix_P3_futur = CalculPrix(prix_standard_biblio)

	### 2ème étape: UPDATE des prix kfet dans la bdd
        querrys = ""
        for produit in prix_P3_futur
            querrys += QUERRY_setMontant(produit[0], produit[1])
        SQL_SELECT(querrys)

    else: # On a arrété le jeu et tout est remis en place, on quitte
        querrys = ""
        for p in produits_standard:
            querrys += QUERRY_setMontant(p["id"],p["prix"])
        SQL_UPDATE(querrys)
        previous_state = isRunning
        break

    sleep(time_period_second)
