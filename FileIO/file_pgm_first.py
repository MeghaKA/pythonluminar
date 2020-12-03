#file operations read,write,append


#step1 create reference
#reference_name=open(filepath,mode_of_operation)
f=open("names","r")
lst=[]
for lines in f:
    lst.append(lines.rstrip("\n"))
print(lst)
#data="\nhello"
#data=data.rstrip("\n")#to  remove \n  fromop
#print(data)

