# from dbconnectpgm.dbconnect import get_connection
import mysql.connector
#we need database connection
from dbconnectpgm.dbconnect import *    #if  outside loc then  dbconnectpgm.dbconnect import */get_connection
                                        #.dbconnect is given because calling pgm is in samelocation

db=get_connection()
cursor=db.cursor()

sql="create table faculty(id varchar(25),name varchar(50),subject varchar(50))"
try:
    cursor.execute(sql)
    print("table successfully created")
except Exception as e:
    print(e.args)
finally:
    db.close()