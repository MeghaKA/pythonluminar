lst=[-2,-1,0,2,3,4]#find least positive missing integer from list
#lst=[120,11,12,13,14]# search for an element
#lst=[10,9,8,11,12,5,6]# find second largest
#asc,desc

#x={1,2,3,3,5}
#san=list(x)
#res=san[3]
#print(res)

cnt=1
for i in range (0,len(lst)):#1 in lst,2 in lst,...5 in lst
    if cnt in lst:#2,3,4,5
        cnt+=1

    else:
        print(cnt,"is least +ve missing integer")
        break








