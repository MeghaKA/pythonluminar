#create a function to perform factorial of a number
def fact(num):
    fact=1
    for i in range(1,(num+1)):
      fact=fact*i
    print(fact)
fact(3)
fact(4)



def add(num1,num2):
    res=num1+num2
    return res
value=add(90,10)
print(value)