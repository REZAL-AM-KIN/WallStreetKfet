from SQL import *
from QUERRY import *


def CalculPrix(produits_standard, A):   # Renvoie [(id1,prix1),(id2,prix2) ...]
    Conso_total_periode = SQL_SELECT(QUERRY_getConsoTotalePeriode())[0][0]
    Conso_total_avant = SQL_SELECT(QUERRY_getConsoTotalePeriodeMoinsUn())[0][0]
    Produits_periode = SQL_SELECT(QUERRY_getIdPrixProduits())
    Produits_periode_futur = []


    # Calul de A
    Lcpp , Lcpa = [], []    # listes consos produits periode et periode avant
    CA_total_Kfet = 0
    for i in range(len(Produits_periode)):
        produit = Produits_periode[i]
        Conso_produit_periode = SQL_SELECT(QUERRY_getConsoPeriode(produit[0]))[0][0]
        Conso_produit_avant = SQL_SELECT(QUERRY_getConsoPeriodeMoinsUn(produit[0]))[0][0]
        Lcpp.append(Conso_produit_periode)  # permet de pas refaire sql
        Lcpa.append(Conso_produit_avant)
        CA_total_Kfet += Lcpp[i] * produits_standard[i][1]

    CA_total_P3 = 0
    for i in range(len(Produits_periode)):
        CA_total_P3 += Lcpp[i] * Produits_periode[i][1]

    A += CA_total_Kfet - CA_total_P3
    print("negats / posits : ", A)
    with open('logA-CA_kfet-CA_P3.txt', "a") as log:
        log.write(str(CA_total_Kfet) + " - " + str(CA_total_P3) + "\n")



    if Conso_total_periode == 0 :
        print("Pas de consos sur la période")

        # on diminue les prix beaucoup car on a trop de CA
        for i in range(len(Produits_periode)):
            if Produits_periode[i][1] > produits_standard[i][1]:
                if A < 0:
                    prix = Produits_periode[i][1] * (1 - COEF_DIMINUTION_CONSO_NULLE * 2)
                else:
                    prix = Produits_periode[i][1] * (1 - COEF_DIMINUTION_CONSO_NULLE)
                prix = max(produits_standard[i][1], int(prix * 100) / 100)
            else:
                prix = Produits_periode[i][1]
            Produits_periode_futur.append((produits_standard[i][0], prix))

        print('consos anciens : ', Lcpa)
        print('conso période :', Lcpp)
        print('prix période : ', Produits_periode)
        print('prix nouveaux : ', Produits_periode_futur)
        return Produits_periode_futur, Lcpp, A


    # terme correctif fixe
    X_fixe = COEF_PHIKS * A / Conso_total_periode
    if A <= 0:
        X_fixe = 0
    print("Correcteur fixe: ", X_fixe)


    for i in range(len(Produits_periode)):

        # calcul de gamma : coeficient de correcteur variable
        if Lcpp[i] < Lcpa[i]:
            gamma = 0

        else:
            cvcp = 0 # somme des conso_verifiant_condition_phi'ks (Lcpp > Lcpa)
            for i_conso in range(len(Produits_periode)):
                if Lcpp[i_conso] >= Lcpa[i_conso]:
                    cvcp += Lcpp[i_conso]
            try:
                gamma = Lcpp[i] / cvcp
            except ZeroDivisionError:
                gamma = 1

        # terme correctif variable spécifique au produit i
        X_var_produit = (1 - COEF_PHIKS) * A * gamma
        if A <= 0:
            X_var_produit = 0

        # terme fixe (ou pas) borné
        X_fixe_produit = min(X_fixe, produits_standard[i][1] * 0.75)

        # Calcul des nouveaux prix
        # si la conso est plus grande que la conso période d'avant, on augmente le prix
        if Lcpp[i] > Lcpa[i]:
            beta = Lcpp[i] / Conso_total_periode
            prix = Produits_periode[i][1] * (1 + COEF_LINGUS_CROISSANT * beta) + X_fixe_produit + X_var_produit

        # si la conso est égale et non nulle, on ne bouge pas le prix, mais on ajuste quand meme avec les correcteurs
        elif Lcpp[i] == Lcpa[i] and Lcpp[i] != 0:
            prix = Produits_periode[i][1] + X_fixe_produit

        # si conso inférieure à la période d'avant ou nulle, on diminue le prix
        else:
            beta = (Conso_total_periode - Lcpp[i]) / Conso_total_periode
            prix = Produits_periode[i][1] * (1 - COEF_LINGUS_DECROISSANT * beta) + X_fixe_produit



        # limites :
        # borne nécessaire pour pas baiser le pg au moment du changement de prix (avant qu'il ait vu)
        # prix min : éviter que le prix soit négatif....
        prix_min = produits_standard[i][1] / 2
        prix = max(prix_min, prix)

        Produits_periode_futur.append((produits_standard[i][0], int(prix * 100) / 100))


    print('consos anciens : ', Lcpa)
    print('conso période :', Lcpp)
    print('prix période : ', Produits_periode)
    print('prix nouveaux : ', Produits_periode_futur)
    return Produits_periode_futur, Lcpp, A