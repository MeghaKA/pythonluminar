n=int(input("enter number"))
sum=0
while(n!=0):
    dig=n%10
    res=res*10+dig
    n=n//10
print(res)