class Parent:
    def m1(self):
        print("print inside parent")


class Child(Parent):
    def m2(self):
        print("print inside Child")


class SubChild(Child):
    def m3(self):
        print("inside subchild")

sb=SubChild()
sb.m3()
sb.m2()
sb.m1()

ch=Child()
#ch.m3()
ch.m2()
ch.m1()

p=Parent()
#p.m3()
#p.m2()
p.m1()