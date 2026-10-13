# Integer

x = 5
if(type(x) is int):
    print("true")
else:
    print ("false")

x = 5.5 
if(type(x) is not float):
    print("true")
else:
    print ("false")


x = 20
y = 20
if(x is y):
    print("x & y is the SAME identity")

y = 30
if(x is not y):
    print("x & y have a  DIFFERENT identity")






# Bitwise Operators

a = 10
b = -10
print("a >> 1 =", a >> 1)
print("b >> 1 =", b >> 1)

a = 5
b = -10

print("a << 1 =", a << 1)
print("b << 1 =", b << 1)
