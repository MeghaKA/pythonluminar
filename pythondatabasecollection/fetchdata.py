from dbconnectpgm.dbconnect import *
db=get_connection()
cursor=db.cursor()
sql="select * from faculty where id='100'"

try:
    cursor.execute(sql)
    # queryset=cursor.fetchall()#fetchone when person  with any  particularid is taken
    queryset=cursor.fetchone()
    print(queryset)
    # #(100,ajay,datastructures)
    # for faculty in queryset:
    #     print("id=",faculty[0])
    #     print("name=",faculty[1])
except Exception as e:
    print(e.args)
finally:
    db.close()
