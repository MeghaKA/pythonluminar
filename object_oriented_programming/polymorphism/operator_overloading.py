class  Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        return Book(self.pages+other.pages)#100+200=300

    def __sub__(self,other):
        return self.pages  -  other.pages

    def __str__(self):
        return str(self.pages)

b1=Book(100)
print(type(b1))
b2=Book(200)
print(type(b2))
# print(b1+b2)#output=__main__object Book at fx35689
# print(b1-b2)
b3=Book(300)
print(b1+b2+b3)#300+b3 int+Book int,int,Book
#+ int,string
#book +book