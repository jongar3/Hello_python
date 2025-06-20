a=[]
b=a
c=[]
print(a is b)
print(a is c)
a.append("a")
print(a is b)
print(b)

b[0]='c'
print(a is b)
print(a[0]+ b[0])
