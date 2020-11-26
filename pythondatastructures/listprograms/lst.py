limit=int(input("enter limit"))
lst=list()
for i in range(1,(limit+1)):
    lst.append(i)
print(lst)

#store even and odd numbers into seperate list
even=[]
odd=[]
for num in lst:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(odd)
print(even)