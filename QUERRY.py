print("SQL Querry initialization ")

## Le schema de la bdd (attention c'est la nouvelle qui n'a pas été mise en place !!) est dispo dans le dossier pour aider

def QUERRY_getIdPrixProduits():
    return (f"SELECT id, prix FROM produits WHERE id IN {id_produit_jeu}";)

def QUERRY_getConsoPeriode(IDproduit): #renvoie le nb vendu sur la periode pour UN PRODUIT
    return (f"SELECT produits_id, count(*) FROM consos WHERE produits_id = {IDproduit} AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < {'00:'+str(time_period)+':00'} ;")

def QUERRY_getConsoTotalePeriode(): #renvoie le nb vendu sur la periode pour TOUS LES PRODUITS en jeu
    return (f"SELECT SUM(count(*)) FROM consos WHERE produits_id IN {id_produit_jeu} AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < {'00:'+str(time_period)+':00'} ;")

def QUERRY_getConsoPeriodeMoinsUn(IDproduit): #renvoie le nb vendu sur la periode pour UN PRODUIT
    return (f"SELECT produits_id, count(*) FROM consos WHERE produits_id = {IDproduit} AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) < {'00:'+str(2*time_period)+':00'} AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) > {'00:'+str(time_period)+':00'} ; ")

def QUERRY_getConsoTotalePeriodeMoinsUn(): #renvoie le nb vendu sur la periode pour TOUS LES PRODUITS en jeu
    return (f"SELECT SUM(count(*)) FROM consos WHERE produits_id IN {id_produit_jeu} AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < {'00:'+str(time_period)+':00'}")

def QUERRY_setMontant(ID,montant):
    return (f"UPDATE produits SET prix={produit["prix"]} WHERE id={produit["id"]};")
