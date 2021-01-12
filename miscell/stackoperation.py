#
size=int(input("enter the size of stack"))
stk=[]
top=0
n=1
def push():
    global top
    top+=1
    print("push...")
def pop():
    print("pop...")
def display():
    print("display...")
while(n!=0):
    option=int(input("enter operation u want to perform 1)push 2)pop 3)display"))
    if(option==1):
        push()
    elif(option==2):
        pop()
    elif(option==3):
        display()
    else:
        print("invalid option")
    n=int(input("enter do u want to continue press 0 or exit"))