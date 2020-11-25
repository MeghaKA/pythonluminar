#*
#**
#***
#****

for row in range(1,5):#row=1,2,3,4
    for col in range(0,row):#col(0,4) col=0,1 col=0,1,2 col=0,1,2,3 col=0,1,2,3,4
        print("*",end=" ")
    print()

for row in range(1,5):#row=1
    for col in range(1,(row+1)):#col(1,2)
        print(col,end=" ")#1
                          #1 2
    print()


for row in range(1,5):
    for col in range(1,8):
        if row==4 or row+col==5or col-row==3:
            print("*",end="")
        else:
            print(end=" ")
    print()