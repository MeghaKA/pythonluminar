class Person:
    def set_Person(self,age,name):
        self.age=age
        self.name=name
    def print_person(self):
        print(self.name,",",self.age)



class Bank(Person):

    Bank_name="sbk"
    @staticmethod
   # def utility_method():
    #    print("utility  method")
    def cube(num):
        print(num**3)
    @classmethod
    def change_Bank_name(cls):
        cls.Bank_name="sbK"
    def  create_account(self,acno,person_name,balance):#,bank_name):
        self.acno=acno
        self.person_name=person_name
        self.balance=balance
        #self.bank_name=bank_name

    def deposit(self,amount):
        self.balance+=amount
        print(Bank.Bank_name,"your account",self.acno,"has been credited with amount",amount,"your aval bal=",self.balance)

    def withdraw(self,amount):

        if (amount>self.balance):
            print("insufficient balance in your account",self.acno,"transaction cancelled")
        else:
            self.balance-=amount
            print("your account",self.acno,"has  been  debited with amount",amount,"your aval bal=",self.balance)
    def  balance_enq(self):
        print("your aval balance",self.balance)

obj=Bank()
obj.set_Person("ajay",66)
obj.print_person()
obj.create_account(1001,"test",5000)#,"sbk")
#Bank.utility_method()
Bank.cube(3)
Bank.change_Bank_name()
print(Bank.Bank_name)
#obj.deposit(5000)
#obj.withdraw(10000)
#obj.balance_enq()



# class
# object
# reference
# different types of variables
# different types of  methods

#how to access instance variablesoutside clas

#print(obj.acno)


#different types of variables

#instance variables
#instance variables are always prepended with self keyword
#we can access instance  variable outside  class by using  reference name

#static  variables
#static  is a keyword  used for efficient  memory utilization
#we can access the static variable using class name


#different  types  of method

#instance method=>deposit,createaccount,balance,withdraw
#static method=>creating some utility  functionalities,@staticmethod
#class  level methods=>manipulating class  levelvaiables,@classmethod

            