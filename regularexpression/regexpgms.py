#regular expression
#used for pattern matching
#step 1
#package not  in builtins.py it is in re
import re
matcher=re.finditer("ab","abababababaabbab")
#                         0123456789
cnt=0
for  match  in matcher:
    print(match.start())#start for knowing matching in which  positions
    #print(match.group())
    cnt+=1
print(cnt)