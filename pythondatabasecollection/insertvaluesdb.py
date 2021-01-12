from dbconnectpgm.dbconnect import *
db=get_connection()
cursor=db.cursor()
id=input('ID:')
f_name=input('Name:')
sub=input('Subject:')
# sql = "insert into faculty(id,name,subject)  values(%s,%s,%s)"
# sql="insert into faculty(id,name,subject)  values('104','ajay','datastructures')"
try:
    # cursor.execute(sql)
    cursor.execute("""
    insert into faculty(id,name,subject)values(%s,%s,%s)""",(id,f_name,sub))
    db.commit()#save  changes to db
    # print("query executed")
    print("success")
except Exception as e:
    print(e.args)
finally:
    db.close()


#html1
#css2
#bootstrap2
#javascript(1 week)
#django
#funbv
#cbv(1 month)

#min4 prjts

