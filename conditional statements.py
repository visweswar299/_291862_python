#boolean expressions
print(5==5)
print(5==6)
print(type(True))
print(type(False))

x=7
if x%2 == 0 :
    print('x is even')
else :
    print('x is odd')


x=4
y=9
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

x=9
y=3
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

if x > y: print("x is greater than y")

#One line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")

#One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
     print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or c > a:
     print("Both conditions are True")

#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
     pass