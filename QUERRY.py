
from WallStreetConfig import *

print("SQL Querry initialization ".format())

# Le schema de la bdd est disponible dans le dossier pour aider
# (attention, c'est la nouvelle qui n'a pas été mise en place !!)

def QUERRY_getIdPrixProduits():
    return ("SELECT id, prix, name "
            "FROM produits "
            "WHERE id IN {0} ;".format(SQLid_produit_jeu))

def QUERRY_getConsoPeriode(IDproduit): # renvoie le nb vendu sur la periode pour UN PRODUIT
    minutes = '{:>2}'.format(PERIOD_SIZE // 60)
    sec = '{:>2}'.format(PERIOD_SIZE % 60)
    return ("SELECT count(*) "
            "FROM consos "
            "WHERE produits_id = {0} "
            "AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < '{1}' ;"
            .format(IDproduit,
                    '00:'+minutes+':'+sec))

def QUERRY_getConsoTotalePeriode(): # renvoie le nb vendu sur la periode pour TOUS LES PRODUITS en jeu
    minutes = '{:>2}'.format(PERIOD_SIZE // 60)
    sec = '{:>2}'.format(PERIOD_SIZE % 60)
    return ("SELECT count(*) "
            "FROM consos "
            "WHERE produits_id IN {0} "
            "AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < '{1}' ;"
            .format(SQLid_produit_jeu,
                    '00:'+minutes+':'+sec))

def QUERRY_getConsoPeriodeMoinsUn(IDproduit):   # renvoie le nb vendu sur la periode pour UN PRODUIT
    # cast all string length to 2 using format
    minutes = '{:>2}'.format(PERIOD_SIZE // 60)
    sec = '{:>2}'.format(PERIOD_SIZE % 60)
    minutesx2 = '{:>2}'.format(PERIOD_SIZE*2 // 60)
    secx2 = '{:>2}'.format(PERIOD_SIZE*2 % 60)
    return ("SELECT count(*) "
            "FROM consos "
            "WHERE produits_id = {0} "
            "AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) < '{1}' "
            "AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) > '{2}' ; "
            .format(IDproduit,
                    '00:'+minutesx2+':'+secx2,
                    '00:'+minutes+':'+sec))

def QUERRY_getConsoTotalePeriodeMoinsUn():  # renvoie le nb vendu sur la periode pour TOUS LES PRODUITS en jeu
    # cast all string length to 2 using format
    minutes = '{:>2}'.format(PERIOD_SIZE // 60)
    sec = '{:>2}'.format(PERIOD_SIZE % 60)
    minutesx2 = '{:>2}'.format(PERIOD_SIZE*2 // 60)
    secx2 = '{:>2}'.format(PERIOD_SIZE*2 % 60)

    return ("SELECT count(*) "
            "FROM consos "
            "WHERE produits_id IN {0} "
            "AND TIMEDIFF( NOW() , FROM_UNIXTIME(date)) < '{1}' "
            "AND TIMEDIFF(NOW(), FROM_UNIXTIME(date)) > '{2}' ;"
            .format(SQLid_produit_jeu,
                    '00:'+minutesx2+':'+secx2,
                    '00:'+minutes+':'+sec))

def QUERRY_setMontant(ID,montant):
    return ("UPDATE produits SET prix={0} WHERE id={1};".format(montant, ID)) # Point virgule important ici
