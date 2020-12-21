class Parent:
    def phone(self):
        print("have nokia 5310")

class Child(Parent):
    def phone(self):
        print("i have iphone12")
    pass
c=Child()
c.phone()