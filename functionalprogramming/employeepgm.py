#find highest salary

class Employee:
    def __init__(self,eid,ename,desig,sal,exp):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.sal=sal
        self.exp=exp

    def  __str__(self):
        return self.ename

#read fromfile
f=open("employee","r")
employees=[]
for lines in f:
    eid,ename,desig,sal,exp=lines.rstrip("\n").split(",")
    employees.append(Employee(eid,ename,desig,sal,exp))

#highest salary
from functools import *
#
# Highsal=reduce(lambda sal1,sal2:sal1 if sal1>sal2  else sal2,
#                list(map(lambda emp:emp.sal,employees)))
# #print  highest salaried employee details
#
# employee=list(filter(lambda emp:emp.sal==Highsal,employees))
# for emp in employee:
#     print(emp.name)

#file read
#object oriented programming
#functional  programming


#find highest  salary  whose designation=developer


developers=list(filter(lambda emp:emp.desig=="developer",employees))

devsalary=list(map(lambda emp:emp.sal,developers))

devhigh=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,devsalary)
print(devhigh)

developer_highest=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
                         list(map(lambda emp:emp.sal,
                                list(filter(lambda emp:emp.desig=="developer",employees)))))
print(developer_highest)