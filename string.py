a="viswa"
print(a)
b='hello'
print(b)
print("Hi welcome to Python's world ");
print("\"Hello World\"");
c="""
Multiline
Strings
"""
print(c)
d='''
another type
Multiline string
'''
print(d)


"""
strings are arrays in Python
"""


a = "Hello, World!"
print(a[1])


'''Looping through strings'''
for x in "banana":
    print(x)

"""
The len() function returns the length of a string:
"""

a = "Hello, World!"
print(len(a))

'''
check string using in keyword
'''

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("Yes, 'expensive' is NOT present.")


'''
slicing strings
'''

b = "Hello, World!"
print(b[2:5])

'''
Get the characters from the start to position 5 (not included):
'''

b = "Hello, World!"
print(b[:5])

'''
Get the characters from position 2, and all the way to the end:
'''
b = "Hello, World!"
print(b[2:])

'''Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):
'''
b = "Hello, World!"
print(b[-5:-2])