num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))

if(num1>num2) & (num1>num3):
    if(num2>num3):
            print("descending order :num1,num2,num3")
            print("ascending order :num3,num1,num2")
    else:
            print("descending order :num1,num3,num2")
            print("ascending order :num2,num3,num1")

elif(num2>num1) & (num2>num3):
    if(num1>num3):

            print("descending order :num2,num1,num3")
            print("ascending order :num3,num1,num2")
    else:
            print("descending order :num2,num3,num1")
            print("ascending order :num1,num3,num2")

elif(num3>num1) & (num3>num2):
    if(num1>num2):
            print("descending order :num3,num1,num2")
            print("ascending order :num2,num1,num3")
    else:
            print("descending order :num3,num2,num1")
            print("ascending order :num1,num2,num3")