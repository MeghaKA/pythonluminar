lst=[6,6,8,9,4,2,3]#7,7,9,10,3,1,2] #if num>5 num+1;num<5 num-1
out=[]
for num in lst:
    if num>5:
        out.append((num+1))
    else:
        out.append((num-1))
print(out)

#out=[num**2 for num in  lst]
#print(out)