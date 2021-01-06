#quantifiers

from  re import *

#pattern="a+"#chk for  a  and  morethan one a
#pattern="a*"#a+ plus zero occurence of a
#pattern="a?"
#pattern="^a"#chk for starting with 'a'


pattern="a$"#ending with a
#pattern='a{2,3}'#chkfor  minimum 2 a andmax 3
#matcter=finditer(pattern,"aaaabaabaaaaa")
matcter=fullmatch(pattern,"baaabaabaaaaabb")
# for match  in matcter:
#     print(match.start())
#     print(match.group())
if  matcter!=None:
    print("given string starting  with a")
else:
    print("given string is not starting  with a")
