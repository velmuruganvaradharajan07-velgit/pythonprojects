a=[1,2,3,4,5,6]
target=10

def sum():
    j=0
    n=0
    i=1
    while j==0:
        c=a[n]+a[i]
        if c==target:
            print(n,i)
        else:
            n += 1
            i += 1
            print(n)
            print(i)
            break



sum()





