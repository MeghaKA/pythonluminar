pattern="ABABAC"
#first recursive character
dict={}
for char in pattern:
    if char not in dict:
        dict[char]=1
    else:
        print(char ,"is  the first  recursive character")
        break