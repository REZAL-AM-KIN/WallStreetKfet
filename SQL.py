def SQL_SELECT(querry):
    _cnx=mysql.connector.connect(host = host, user = user, password = password, database = database)
    _cursor=_cnx.cursor()
    _cursor.execute(querry)
    _select=_cursor.fetchall()
    _cnx.close()
    return _select

def SQL_UPDATE(querry):
    _cnx=mysql.connector.connect(host = host, user = user, password = password, database = database)
    _cursor=_cnx.cursor()
    querrys=querry.split(";")
    print("Synchronisation SQL: "+str(len(querrys))+" requetes")
    n=len(querrys)
    for i in range(len(querrys)):
        hint("SYNCH SQL "+str(i)+" / "+str(n),4)
        q=querrys[i]
        _cursor.execute(q)
        _cnx.commit()
    _cnx.close()
    DATA_add('/home/rezal/WallStreetMode/LOG_SQL.txt',querry+"\n")
