f=open("employee","r")

emp_dict={}
for lines in f:
    print(lines)
    data=lines.rstrip("\n").split(",")


    if id not in emp_dict:
        emp_dict[data[0]]={"id":data[0],"name":data[1],"desig":data[2],"exp":data[3],"salary":data[4]}
print(emp_dict)
