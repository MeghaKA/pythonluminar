#prime number?...7(1,7) 7 isprime number

#15(1,3,15)not prime

#7
#1,7 exclude
number=int(input("enter number"))
flag=0
for i in range (2,number):
        if(number%i==0):
                flag=1
                break
        else:#flag=0
            flag=0
if(flag==0):
        print("prime number")
else:
        print("not prime number")