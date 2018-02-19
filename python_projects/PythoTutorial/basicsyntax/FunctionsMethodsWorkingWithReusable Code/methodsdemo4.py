"""
Variable Scope
"""

a = 10

def method(a):
    print("Value of local 'a' is: " + str(a))
    a = 2
    print("New value of local 'a' is: " + str(a))

print("Value of global 'a' is: " + str(a))
method(a)
print("Did the value of global 'a' change? " + str(a))

print("*"*40)
a = 10

def method():
    global a
    print("Value of 'a' inside the method is: " + str(a))
    a = 2
    print("New value of 'a' inside the method is changed to: " + str(a))

print("Value of global a is: " + str(a))
method()
print("Did the value of global 'a' change? " + str(a))