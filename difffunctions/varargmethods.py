#def  add (num1,num2):
#       res=num1+num2
#       print(res)

#add(10,20)

#variable length argument methods


#def add(*args):
#   print(args)

#add(10,58)
#add(47,88,66)


def add (*args):
    total=0
    for num in args:
        total+=num
    print(total)
add(10,20)
add(10,29)
add(26,34,86,37)
add(28,38,11,23,45)
#*args accepts in tuple format
#**args accempts  in the dictionary form

def printEmp(**args):
    print(args)

printEmp(home="Kakkanad",name="ajay",wrking="aluva")