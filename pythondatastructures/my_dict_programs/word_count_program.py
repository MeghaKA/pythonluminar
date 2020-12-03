text="hello hai hai hello hai"
#o/p  hello:2 hai:3
words=text.split(" ")
#print(words)
dict={}
#{hello:2,hai:3}
#dict[word]=1#{hello:1} if that word is notin dictionary
#dict[word]+=1#if that wordis in dictonary
for word in  words:#"hello"
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
