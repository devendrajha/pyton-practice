x=10
x+=20
print(x)
x*=20
print(x)

y=0b111
y >>= 0b1000
print(y)

'''
# Ternary Operator OR Conditional Operator
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
max=a if a>b and a>c else b if b>c else c
print("Maximum Value:",max)
'''

#Identity Operators
a=10
b=11
print(a is b)
x="True"
y="True"
print(id(x))
print(id(y))
print( x is y)
print("------------------------------------------")


list1=["one","two","three"]
list2=["one","two","three"]
list3=["one","two","three"]
print(id(list1))
print(id(list2))
print(id(list3))
print(list1 is list2)
print(list1 is not list2)
print(list1 == list2)
print("------------------------------------------")

list1=["sunny","bunny","chinny","pinny"]
print("sunny" in list1)

import math
print(math.sqrt(16))

print(math.sin(90))
"""
a,b= [print(int(x)) for x in input("Enter 2 numbers :").split()]
print("Product is :", a*b)
"""
x = eval("10+20+30.5")
print(x)
print (type(x))