#multiplication of two numbers
"""
Exercise 1: Calculate the multiplication and sum of two numbers
"""

a=int(input("Enter the number one"))

b=int(input("Enter the number two"))

c=a*b

if c<=1000:
    print("The product of two number is",c)
else:
    d=a+b
    print("The sum of two numbber",d)