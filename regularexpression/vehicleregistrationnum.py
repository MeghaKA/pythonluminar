#KL08BS1375->VALID
#GJ08BN211->INVALID

f=open("registrationnumbers","r")
fout=open("validreg","w")

regnum=set()
for numbers in f:
    regnum.add(numbers.rstrip("\n"))



from re import *
rule="KL\d{2}[A-Z]{1,2}\d{1,4}"

for vehiclenum in regnum:

#vehiclenum=input("enter vehicle registration number")

    matcher=fullmatch(rule,vehiclenum)
    if matcher!=None:
        fout.write(vehiclenum +"\n")
        #print("valid vehicle number")
    else:
        pass
        #print("invalid registration number")



#create rule for validating gmail ids implementing in file
#validate all phone numbers

#beautifulsoup bs4
#
#exception handling
#mysql(create,insert,uupdate,delete)