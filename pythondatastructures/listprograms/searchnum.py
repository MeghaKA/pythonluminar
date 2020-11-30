lst=[120,11,12,13,14]# search for an element
#linearsearch

element=int(input("enter element for searching"))#12
#if (element in lst):
#     print("element found")
# else:
#   print("element not found")
flg=0
for num  in lst:
    if(num==element):
        flg+=1
        break
    else:
        flg=0
if(flg>0):
    print("element found")
else:
    print("element not found")

