num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
if(num1>num2)&(num1>num3):
    print("num1,"," is greater ")

elif(num2>num3)&(num2>num1):
        print("num2,"," is greater")

elif(num3>num1)&(num3>num2):
        print("num3,"," is greater")

else:
        print("numbers,"," are equal")

        print("it is the second largest number")