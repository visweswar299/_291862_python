#while loop

#Print i as long as i is less than 6:

i = 1
while i < 6:
     print(i)
     i += 1

#Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#else condition
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


print('''
For loops
''')
'''
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
for x in "banana":
  print(x)

#Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Using the range() function:

for x in range(6):
  print(x)

#Using the start parameter:

for x in range(2, 6):
  print(x)

#Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)

#else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#pass statement
for x in [0, 1, 2]:
  pass