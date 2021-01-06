f=open("out.txt","w")

lst=["aji","anu","arin"]
f.write("hello")
f.close()

for names in lst:
    f.write(names+"\n")