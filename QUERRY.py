print("SQL Querry initialization ")

## Le schema de la bdd (attention c'est la nouvelle qui n'a pas été mise en place !!) est dispo dans le dossier pour aider

def QUERRY_getIdPrixProduits():
    return (f"SELECT id, prix FROM produits WHERE id IN {SQLid_produit_jeu} ;")

def QUERRY_getConsoPeriode(IDproduit): #renvoie le nb vendu sur la periode pour UN PRODUIT
    if time_period >= 10:
        return (f"SELECT count(*) FROM consos WHERE produits_id = {IDproduit} AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < '{'00:'+str(time_period)+':00'}' ;")
    else :
        return (f"SELECT count(*) FROM consos WHERE produits_id = {IDproduit} AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < '{'00:0'+str(time_period)+':00'}' ;")

def QUERRY_getConsoTotalePeriode(): #renvoie le nb vendu sur la periode pour TOUS LES PRODUITS en jeu
    if time_period >= 10:
        return (f"SELECT count(*) FROM consos WHERE produits_id IN {SQLid_produit_jeu} AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < '{'00:'+str(time_period)+':00'}' ;")
    else:
        return (f"SELECT count(*) FROM consos WHERE produits_id IN {SQLid_produit_jeu} AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < '{'00:0'+str(time_period)+':00'}' ;")

def QUERRY_getConsoPeriodeMoinsUn(IDproduit): #renvoie le nb vendu sur la periode pour UN PRODUIT
    if time_period >= 10 :
        return (f"SELECT count(*) FROM consos WHERE produits_id = {IDproduit} AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) < '{'00:'+str(2*time_period)+':00'}' AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) > '{'00:'+str(time_period)+':00'}' ; ")
    elif time_period >= 5:
        return (f"SELECT count(*) FROM consos WHERE produits_id = {IDproduit} AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) < '{'00:'+str(2*time_period)+':00'}' AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) > '{'00:0'+str(time_period)+':00'}' ; ")
    else :
        return (f"SELECT count(*) FROM consos WHERE produits_id = {IDproduit} AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) < '{'00:0'+str(2*time_period)+':00'}' AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) > '{'00:0'+str(time_period)+':00'}' ; ")

def QUERRY_getConsoTotalePeriodeMoinsUn(): #renvoie le nb vendu sur la periode pour TOUS LES PRODUITS en jeu
    if time_period >= 10:
        return (f"SELECT count(*) FROM consos WHERE produits_id IN {SQLid_produit_jeu} AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < '{'00:'+str(2*time_period)+':00'}'AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) > '{'00:'+str(time_period)+':00'}' ;")
    elif time_period >= 5:
        return (f"SELECT count(*) FROM consos WHERE produits_id IN {SQLid_produit_jeu} AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < '{'00:'+str(2*time_period)+':00'}'AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) > '{'00:0'+str(time_period)+':00'}' ;")
    else:
        return (f"SELECT count(*) FROM consos WHERE produits_id IN {SQLid_produit_jeu} AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < '{'00:0'+str(2*time_period)+':00'}'AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) > '{'00:0'+str(time_period)+':00'}' ;")

def QUERRY_setMontant(ID,montant):
    return (f"UPDATE produits SET prix={montant} WHERE id={ID};") # Point virgule important ici
