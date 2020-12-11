f=open("complete_csv")
dict={}
for lines in f:
    print(lines)
    data=lines.rstrip("\n").split(",")
    print(data)
    state=data[1]
    confirmed_cases=data[4]
    if state not in dict:
        dict[state]=int(confirmed_cases)
    else:
        dict[state]=int(confirmed_cases)
for k,v in dict.items():
    print(k,v)

highest=max(dict,key=dict.get)
print("highest",highest,dict[highest])

lowest=min(dict,key=dict.get)
print("lowest",lowest,dict[lowest])

srt=sorted(dict,key=dict.get,reverse=True)
print("sorted","-",srt)