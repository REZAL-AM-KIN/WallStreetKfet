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
        print(QUERRY_getConsoPeriode(produit[0]))
        Conso_produit_periode = SQL_SELECT(QUERRY_getConsoPeriode(produit[0]))
        print(Conso_produit_periode)
        Conso_produit_periode = Conso_produit_periode[0][0]
        Conso_produit_avant = SQL_SELECT(QUERRY_getConsoPeriodeMoinsUn(produit[0]))[0][0]
        Lcpp.append(Conso_produit_periode)  # permet de pas refaire sql
        Lcpa.append(Conso_produit_avant)
        CA_total_Kfet += Lcpp[i] * produits_standard[i][1]

    if Conso_total_periode == 0:
        print("Pas de consos sur la période")
        return Produits_periode, Lcpp

    CA_total_P3 = 0
    for i in range(len(Produits_periode)):
        CA_total_P3 += Lcpp[i] * Produits_periode[i][1]

    A = CA_total_Kfet - CA_total_P3
    with open('logA-CA_kfet-CA_P3.txt', "a") as log:
        log.write(str(CA_total_Kfet) + " - " + str(CA_total_P3)+ "\n")

    for i in range(len(Produits_periode)):

        # si la conso est plus grande que la conso période d'avant, on augmente le prix
       if Lcpp[i] >= Lcpa[i]:
           beta = Lcpp[i] / Conso_total_periode
           Produits_periode_futur.append((produits_standard[i][0], Produits_periode[i][1] * (1 + COEF_PHIKS * beta)))

       # sinon, on diminue le prix
       else:
           beta = (Conso_total_periode - Lcpp[i]) / Conso_total_periode
           Produits_periode_futur.append((produits_standard[i][0], Produits_periode[i][1] * (1 - COEF_PHIKS * beta)))


    print('consos anciens : ', Lcpa)
    print('conso période :', Lcpp)
    print('prix période : ', Produits_periode)
    print('prix nouveaux : ', Produits_periode_futur)
    return Produits_periode_futur, Lcpp, A