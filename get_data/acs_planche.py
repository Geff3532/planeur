import mysql.connector as mysql
import datetime

def is_flying(immat):
    db = mysql.connect(host="localhost",user='root',password='',db='test')
    cursor = db.cursor()
    date = datetime.date.today()
    cursor.execute( ("SELECT * FROM acs_planche WHERE Reg = %s AND day = %s"),(immat,date) )
    table = cursor.fetchall()
    cursor.close()
    if len(table) == 0:
        return False
    else:
        table.sort(key=lambda u:u[3],reverse=True)
        if table[0][5] == None:
            return True
        return False
    
    