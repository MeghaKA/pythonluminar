class Maths: # to make fn overloading  remove class
    def add(self):#add()
        print("inside no arg add method")
    def add(self,num1):#add(num1)
        print("inside single arg add method")
    def add(self,num1,num2):#add(num1,num2)
        print("inside two arg add  method")

#same method  name different number of arguments

m=Maths()#in fn overloading  it will be not present

m.add(10,29)
#m.add(10)