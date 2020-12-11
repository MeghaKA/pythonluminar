#class
    #plan,design pattern,template,blueprint

#object
    #real world entity

#reference?
    #operationperformed  on object


#class Classname:
class Person:
    #attribute ofperson self.name,self.age,self.gender
    def set_Person(self,name,age,gender):
        #attribute set_person initializes attributes of person
        self.name=name
        self.age=age
        self.gender=gender


    def print_Person(self):#print_person and set_person are methods
        print("name",self.name)
        print("age",self.age)
        print("gender",self.gender)

#reference_name=class()
obj=Person()
obj.set_Person("ajay",25,"male")
obj.print_Person()

#self is a key word used to print current class oject
obj1=Person()
obj1.set_Person("vijay",26,"male")
obj1.print_Person()