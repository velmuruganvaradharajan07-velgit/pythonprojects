'''Exercise 3: Print characters present at an even index number'''

a=input("Enter the character")
b=list(a)
c=len(b)
print(c)
for x in range(c):
    #print(x)
    if x%2==0:
        print(b[x])