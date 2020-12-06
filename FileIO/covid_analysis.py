f=open("complete_csv")
dict={}
for lines in f:
    print(lines)
    data=lines.rstrip("\n").split(",")
    print(data)
    state=data[1]
    confirmed_cases=data[4]
    if state not in dict:
        dict[state]=confirmed_cases
    else:
        dict[state]=confirmed_cases
for k,v in dict.items():
    print(k,v)


