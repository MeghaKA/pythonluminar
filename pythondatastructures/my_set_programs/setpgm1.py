#st=set()         #empty set define using{}
#print(type(st))

st={10,20,30,45,30,40,50}
st1={100,20,300}
#st.update(st1)
#print(st)
diff=st.difference(st1)
print(diff)

unionset=st.union(st1)
print(unionset)

intersection=st.intersection(st1)
print(intersection)