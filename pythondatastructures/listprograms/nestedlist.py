students=[[1001,"ajay","mca",150],
          [1002,"vijay","bca",145],
          [1003,"arun","mca",150],
          [1004,"amal","bca",135]]
#print all student name
for student in students:
    print(student[1])

#print all  student  roll  number
for student in students:
    print(student[0])

#print all student details whose course="mca"
for student in students:
    if student[2]=='mca':
        print(student)

#print all student details whose total>140
for student in students:
    if student[3]>140:
        print(student)

#find total sum  of  student  total group by course
totalmc=0
totalbc=0
for student in students:
    if student[2]=='mca':
        totalmc+=student[3]
    elif student[2]=='bca':
        totalbc+=student[3]
print("mca whole total",totalmc)
print("bca whole total",totalbc)

