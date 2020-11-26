#define by using []or by using list()
#insertion order is preserved
#updation possible
#duplicates are allowed
lst=["java","python","c#","javascript","python","python"]

#adding new element

#lst.insert(3,"perl")
#print(lst)
#lst.append("dart")
#print(lst)
#lst[0]="ruby"
##print(lst)

#       0       1      2      3
print(lst[0])
print(lst[-1:-5:-1])#slicing
print(lst[1:3])
print(lst[0:2])
print(lst[:3])

#[low:upper:step]
print(lst[0:4:2])

#iteration
#for item in lst:
 #   print(item)


#marks=list()
#insert some values
#perform slicing
#update a object

marks=[10,28,90,100]
#marks.insert(3,47)
#marks.insert(4,45)
#marks.append(30)
#print(marks)
print(marks[0])
print(marks[2:4])
print(marks[-3:-1])
print(marks[-2:-4:-2])