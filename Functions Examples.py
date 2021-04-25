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

def function5(**student):
    """If the number of keyword arguments is unknown, add a double ** before the parameter name"""
    print("He's last name is "+student["lname"])
print(function5.__doc__)
function5(fname="Viswa",lname="Reddy")

def function6(State="AP"):
    """Default parameter value"""
    print("I'm from "+State)
print(function6.__doc__)
function6()
function6("Kerala")
function6("Banglore")
function6("Tamilnadu")

def function7(smoothies):
    """Passing a List as an argument"""
    for x in smoothies:
        print(x)
juices=["Mango juice","Grape juice", "Apple juice"]
print(function7.__doc__)
function7(juices)

def function8(value):
    """Return Values"""
    return value**value
print(function8.__doc__)
print(function8(5))
print(function8(1))
print(function8(10))