#create dictemployeemust have keys eid,emp_name,desig,salary"
#"print employee name"
#"check exp key  is there"
#"add exp key"

emp={"eid":100,"emp_name":'amal',"desig":'engineer',"salary":30000}
print(emp["emp_name"])

if ("exp"  in  emp):
       print(emp["exp"])
else:
    emp["exp"] = 3
    print(emp)
#add  salary+5000

emp["salary"]+=5000
print(emp)
