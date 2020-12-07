students={
    100:{"rol":100,"name":"ajay","total":140,"course":"bca"},
    101:{"rol":101,"name":"vijay","total":145,"course":"bca"},
    102:{"rol":102,"name":"anu","total":130,"course":"bca"},
    103:{"rol":103,"name":"jino","total":135,"course":"mca"},
}


print(students[100])
#print name  only
print(students[100]["name"])
print(students[100]["total"])


#def printstudents():

  #   printstudents(rol=100)#it will print  name  regarding  roll=100
 #   printstudents(rol=100,property="course")#it  have to print student name  along with his total

#ajay,bca

#def printstudents(**args):
 #   print(args)
#printstudents(id=100,property="course")



def printstudents(**kwargs):#{id:101}
   # print(kwargs)#(not needed here)
    id=kwargs.get("id")#100 id=kwargs[id"] 101
    if(id in students):
        if"property" in kwargs:
            prop=kwargs.get("property")#total
            if prop in students[id]:
                print(students[id][prop])

        print(students[id]["name"])
    else:
        print("student with this rol not exist")

#printstudents(id=109)
printstudents(id=100,property="total")
