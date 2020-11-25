low=10
upp=50
for num in range(10,51):
    flag=0
    for i in range(2,num):
        if num % i == 0:
            flag=1
            break
    if(flag==0):
        print(num)