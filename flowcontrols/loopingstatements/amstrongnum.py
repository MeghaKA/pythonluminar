number=int(input("enter the number"))#123
res=0
while(number!=0):
        dig=number%10
        res=res+(dig**3)
        number=number//10
print(res)