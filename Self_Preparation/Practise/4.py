a=input("Enter the name")
b=int(input("Entetr the number"))
c=list(a)
for x in range (b):
    c.remove(a[x])

#print(c)
d="".join(c)
print(d)