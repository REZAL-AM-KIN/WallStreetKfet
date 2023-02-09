import time
from datetime import datetime
import pickle

from SQL import *
from QUERRY import *
from model import CalculPrix

# import config
from WallStreetConfig import *

#Ici c'est le coeur du truc, qui va tourner en fond et gérer la soirée

isRunning = True

# on initialise le CA
A = 0

periodes_jouees = 0
while True:
    if periodes_jouees >= GAME_DURATION_STEP:
        isRunning = False
    periodes_jouees += 1

    print(datetime.now().strftime("%H:%M:%S"))

    if isRunning != previous_state:     # permet de constater que le jeu démarre ou s'arrête

        if isRunning:   # si c'est un démarrage, on stocke les bons prix
            produits_standard = SQL_SELECT(QUERRY_getIdPrixProduits())
            # print(produits_standard)
            for produit in produits_standard:
                name_produit.append(produit[2])

            with open("name_produit.txt", 'wb') as fp:
                pickle.dump(name_produit, fp)

            with open('logA-CA_kfet-CA_P3.txt', "w") as log:
                log.write("CA_total_Kfet - CA_total_P3\n")

            print("\nLes produits joués sont: ", name_produit, "\n")
        previous_state = isRunning

    if isRunning:   # On a deja demarré et on est en jeu
        # -------------------
        # 1ème étape: Calcul des nouveaux prix à partir des formules de scientifiques notables du 21e.
        prix_p3_futur, Lcpp_temp, A = CalculPrix(produits_standard, A - NEGATS_PAR_PAS)
        all_Lccp.append(Lcpp_temp)
        all_prix.append([item[1] for item in prix_p3_futur])
        with open("all_lccp.txt", 'wb') as fp:
            pickle.dump(all_Lccp, fp)
        with open("all_prix.txt", 'wb') as fp:
            pickle.dump(all_prix, fp)
        with open("all_lccp.txt", "rb") as fp:
            test = pickle.load(fp)
        #print(all_Lccp,all_prix)
        #print("test:",test)

        # -------------------
        # 2ème étape: UPDATE des prix kfet dans la bdd
        querrys = ""
        for produit in prix_p3_futur:
            querrys += QUERRY_setMontant(produit[0], produit[1])
        SQL_UPDATE(querrys)

    else:   # On a arrété le jeu et tout est remis en place, on quitte
        querrys = ""
        for produit in produits_standard:
            querrys += QUERRY_setMontant(produit[0], produit[1])
        SQL_UPDATE(querrys)
        with open('logA-CA_kfet-CA_P3.txt', "a") as log:
            log.write("A: " + str(A) + "\n")
        print("\nremise à zero prix")
        previous_state = isRunning
        break

    # Le negat's est trop important. Le jeu est stoppé et tout est remis en place, on quitte
    if A + periodes_jouees * NEGATS_PAR_PAS > NEGATS_P3:
        querrys = ""
        for produit in produits_standard:
            querrys += QUERRY_setMontant(produit[0], produit[1])
        SQL_UPDATE(querrys)
        print("\nremise à zero prix")
        previous_state = isRunning
        break


    print("\nIl reste {0} manches de {1} secondes.\n".format(1+GAME_DURATION_STEP - periodes_jouees, REFRESH_INTERVAL))
    time.sleep(REFRESH_INTERVAL)    # on attends le step suivant
