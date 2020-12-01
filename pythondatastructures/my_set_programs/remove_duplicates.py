#lst=[10,10,20,30,40,50,50,51,51,52]
#st=set(lst)
#lst=list(st)
#print(lst)


names=["a","b","c","d","e","f"]
passed=["a","b","c"]
st=set(names)
st1=set(passed)
failed=st-st1
print(failed)



