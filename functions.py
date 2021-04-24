def add(a,b):
    """this function returns sum of two numbers"""
    return a+b
    print(a+b)
a=int(input("Enter the value:"))
b=int(input("ENter the value:"))
c=add(a,b)
print(c)
print(add.__doc__)



a=int(input("Enter the value:"))
b=int(input("ENter the value:"))
d=print(sum((a,b)))