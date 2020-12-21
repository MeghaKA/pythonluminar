class Person:
    def __init__(self,age,name):
        self.name=name
        self.age=age

    def __str__(self):#tostring method string representation of an object
        #return str(self.age)
        return self.name
p=Person(25,"person1")

#if we are  printing an object __str__()method  will execute


print(p)