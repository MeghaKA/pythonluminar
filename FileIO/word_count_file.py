f=open("word_data")

dict={}
for  lines in f:
    words=lines.rstrip(".\n").split(" ")
    for word in words:
        word=word.rstrip(",")
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
for k,v in dict.items():
    print(k,v)

highest=max(dict,key=dict.get)
print(highest,dict[highest])

#lst=[10,11,12,13,15,20]
#print(max(lst))
#highest=max(dict,key=dict.get)
#my_dict={"roll":1001,"name":"ajay"}
#print(my_dict.get("roll"))

