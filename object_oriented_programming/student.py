#create a classstudent consist of attributesrol,name,course,total


#must  have methods for setting and printing these  attributes

class Student:

    def set_Student(self,rol,name,course,total):
        #instance variabesself.rol,self.name.self.course,self.total
        self.rol=rol
        self.name=name
        self.course=course
        self.total=total

    def print_Student(self):
        print("rol",self.rol)
        print("name",self.name)
        print("course",self.course)
        print("total",self.total)


obj=Student()
obj.name="jino"
obj.rol=66
obj.course="mca"
obj.total=999
#obj.set_Student(2,"ajay","cs",445)
obj.print_Student()

#we can accessinstance variableoutside classby using  reference

#print(obj.course)