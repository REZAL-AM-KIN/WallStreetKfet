print("SQL Querry initialization ".format())

## Le schema de la bdd (attention c'est la nouvelle qui n'a pas été mise en place !!) est dispo dans le dossier pour aider

def QUERRY_getIdPrixProduits():
    return ("SELECT id, prix, name FROM produits WHERE id IN {0} ;".format(SQLid_produit_jeu))

def QUERRY_getConsoPeriode(IDproduit): #renvoie le nb vendu sur la periode pour UN PRODUIT
    if time_period >= 10:
        return ("SELECT count(*) FROM consos WHERE produits_id = {0} AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < '{1}' ;".format(IDproduit,'00:'+str(time_period)+':00'))
    else :
        return ("SELECT count(*) FROM consos WHERE produits_id = {0} AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < '{1}' ;".format(IDproduit,'00:0'+str(time_period)+':00'))

def QUERRY_getConsoTotalePeriode(): #renvoie le nb vendu sur la periode pour TOUS LES PRODUITS en jeu
    if time_period >= 10:
        return ("SELECT count(*) FROM consos WHERE produits_id IN {0} AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < '{1}' ;".format(SQLid_produit_jeu,'00:'+str(time_period)+':00'))
    else:
        return ("SELECT count(*) FROM consos WHERE produits_id IN {0} AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < '{1}' ;".format(SQLid_produit_jeu,'00:0'+str(time_period)+':00'))

def QUERRY_getConsoPeriodeMoinsUn(IDproduit): #renvoie le nb vendu sur la periode pour UN PRODUIT
    if time_period >= 10 :
        return ("SELECT count(*) FROM consos WHERE produits_id = {0} AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) < '{1}' AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) > '{2}' ; ".format(IDproduit,'00:'+str(2*time_period)+':00','00:'+str(time_period)+':00'))
    elif time_period >= 5:
        return ("SELECT count(*) FROM consos WHERE produits_id = {0} AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) < '{1}' AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) > '{2}' ; ".format(IDproduit,'00:'+str(2*time_period)+':00','00:0'+str(time_period)+':00'))
    else :
        return ("SELECT count(*) FROM consos WHERE produits_id = {0} AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) < '{1}' AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) > '{2}' ; ".format(IDproduit,'00:0'+str(2*time_period)+':00','00:0'+str(time_period)+':00'))

def QUERRY_getConsoTotalePeriodeMoinsUn(): #renvoie le nb vendu sur la periode pour TOUS LES PRODUITS en jeu
    if time_period >= 10:
        return ("SELECT count(*) FROM consos WHERE produits_id IN {0} AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < '{1}'AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) > '{2}' ;".format(SQLid_produit_jeu,'00:'+str(2*time_period)+':00','00:'+str(time_period)+':00'))
    elif time_period >= 5:
        return ("SELECT count(*) FROM consos WHERE produits_id IN {0} AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < '{1}'AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) > '{2}' ;".format(SQLid_produit_jeu,'00:'+str(2*time_period)+':00','00:0'+str(time_period)+':00'))
    else:
        return ("SELECT count(*) FROM consos WHERE produits_id IN {0} AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < '{1}'AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) > '{2}' ;".format(SQLid_produit_jeu,'00:0'+str(2*time_period)+':00','00:0'+str(time_period)+':00'))

def QUERRY_setMontant(ID,montant):
    return ("UPDATE produits SET prix={0} WHERE id={1};".format(montant,ID)) # Point virgule important ici
