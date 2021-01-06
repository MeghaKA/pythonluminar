# lst=[10,11,12,13,14,15]
#
# #squares
# #map(function,iterable)
#
# squares=list(map(lambda no:no**2,lst))
# print(squares)
#
# cubes=list(map(lambda no:no**3,lst))
# print(cubes)
#
# #filter
# #fetch only even numbers
#
# even=list(filter(lambda no:no%2==0,lst))
# print(even)
#
# names=["ajay","abhi","bincy","aji","anu"]
#
# na=list(map(lambda name:name.upper(),names))
# print(na)
#
# aname=list(filter(lambda name:name[0]=='a',names))
# print(aname)

#map,filter all are  class/functions


#reduce=sum,min,max

#sum

from functools import *
lst=[10,11,12,13,14,15]

#sum of even numbers

evensum=reduce(lambda no1,no2:no1+no2,list(filter(lambda no:no%2==0,lst)))
print(evensum)
#minimum of even number
evenmin=reduce(lambda no1,no2:no1 if no1<no2 else no2,list(filter(lambda no:no%2==0,lst)))
print(evenmin)

sum=reduce(lambda no1,no2:no1+no2,lst)
print(sum)

min=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(min)
max=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(max)
