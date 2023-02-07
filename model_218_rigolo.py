from SQL import *
from QUERRY import *


def CalculPrix(produits_standard):   # Renvoie [(id1,prix1),(id2,prix2) ...]
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
        CA_total_Kfet += Lcpp[i]*produits_standard[i][1]

    if Conso_total_periode == 0:
        print("Pas de consos sur la période")
        return Produits_periode, Lcpp

    CA_total_P3 = 0
    for i in range(len(Produits_periode)):
        CA_total_P3 += Lcpp[i]*Produits_periode[i][1]

    A = CA_total_Kfet - CA_total_P3
    with open('logA', "a") as log:
        log.write(str(CA_total_Kfet) + " - " + str(CA_total_P3))

    for i in range(len(Produits_periode)):
        #Calcul des nouveaux prix
        if Lcpp[i] == 0:
            x = 0
        else:
            x = A / Lcpp[i]


        if Lcpp[i] > Lcpa[i]:
            #print(int(produits_standard[i][1]*(1+(Lcpp[i]/Conso_total_periode))*100)/100)
            # print(Conso_produit_periode)
            # print(Conso_total_periode)
            Produits_periode_futur.append((produits_standard[i][0], max(int(100*produits_standard[i][1]/2)/100,
                                                                        int((produits_standard[i][1] + (Lcpp[i] / Conso_total_periode) * coef_lingus) * 100) / 100)))
        else:
            Produits_periode_futur.append((produits_standard[i][0], max(int(100*produits_standard[i][1]/2)/100,
                                                                        int((produits_standard[i][1] - (1 - Lcpp[i] / Conso_total_periode) * coef_lingus) * 100) / 100)))
    print('consos anciens : ', Lcpa)
    print('conso période :', Lcpp)
    print('prix période : ', Produits_periode)
    print('prix nouveaux : ', Produits_periode_futur)
    return Produits_periode_futur, Lcpp