def function1():
    """Creating and calling a function"""
    print("Welcome to the functions!")
print(function1.__doc__)
function1()

print("""
From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called. 
""")

def function2(name):
    """calling function with arguments"""
    print("Hi "+name+".")
print(function2.__doc__)
function2("Viswa")

def function3(fname,lname):
    """calling function with two arguments"""
    print("Hi "+fname+" "+lname)
print(function3.__doc__)
function3("Viswa","reddy")

def function4(*name):
    """Number of arguments is unknown then add a * before parameter name"""
    print("The name is:"+name[1])
print(function4.__doc__)
function4("viswa","paddu","siva","chandra")