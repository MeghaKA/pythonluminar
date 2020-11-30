#employees=[[1001,"ajay","qa",15000],
#           [1002,"vijay","developer",25000],
 #          [1003,"arun","ba",15000],
  #         [1004,"amal","developer",30000]]
#print all employee id

#find total of salary


#find how  many members working as developer

#findtotal  of salary group by designation
#qasum=0
#dsum=0
#for employee in employees:
 #   if(employee[2]=="qa"):
  #      qasum+=employee[3]
   # elif(employee[2]=="developer"):
    #    dsum+=employee[3]
#print(dsum)
#print(qasum)

employees=[[1001,"ajay","qa",1981,2003],
          [1002,"vijay","developer",1992,2008],
          [1003,"arun","ba",2009,2014],
         [1004,"amal","developer",1987,1989]]

for employee in employees:
    print(employee[2])

for employee in employees:
    if employee[2]=='developer':
       print(employee)

for employee in employees:
    if employee[3]<=1990:
        print(employee)

for employee in employees:
    if employee[4]-employee[3]>9:
        print(employee)


#print all employee designation
#print  all employee whose designation=developer

#print all emloyee those  whoareworking in 1980's

#print all emploee details whose experience>9years