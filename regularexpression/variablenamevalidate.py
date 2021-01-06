#variable name rule
#starting with  a-k
#second character should be a digit and it mustbe divisdible by 3
#followedby any number ofcharacters
#z2rggg =>invalid
#87vggg =>invalid
#a3rgggg=>vcalid
from re import *
    #rule='[a-kA-K][369][a-zA-Z0-9]*'
rule='[a-kA-K][369]\w*'
variablename=input("enter variable name")
matcher=fullmatch(rule,variablename)
if matcher !=None:
    print("valid variable name")
else:
    print("invalid")