#values are stored in dictionary in the form of key,value pairs

#rol:100,name:ajay,course:bca
#rol,name,course


students={100:{"rol":100,"name":"ajay","course":"bca","total":150},
          101:{"rol":101,"name":"vijay","course":"mca","total":145}}#array,queue,stack(push,pop)
#students["total"]+=50
#print(students)

#print student name  "ajay"
#ajay is  a value ,tofetch value  we have touse corresponding key
#print(students["name"])
# #course
# print(students["course"])

#for key in students:
#    print(key,students[key])#rol,name,course

#duplicate  values allowded,duplicate keys not allowded
#for k,v in students.items():
#    print(k,v)
#students["name"]="AJAY"
#print(students) #posibletoupdate dictionaries

#checking for specifickey
#print("rol"in students)

#checkingfor totalkey
#if ("total" not in  students):
 #   students["total"]=150
  #  print(students)
