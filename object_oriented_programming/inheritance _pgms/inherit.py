#inheritance
#parent-base-super
#child-derived-subclass

class Parent:
    def phone(self):
        print("i have nokia  5318")
    def __lap_top(self):
        print("i hav laptop")
class Child(Parent):
    def bike(self):
        print("i have duke")
    def change_bike(self,num):
        self.bike_num=num
    def print_show_num(self):
        print(self.bike_num)

ch=Child()
ch.phone()
ch.bike()

# Child().bike()
# Child().change_bike(250)
#
# Child().bike()
# Child().print_show_num()

#__is a special  method and  used  for checking whether to make it private