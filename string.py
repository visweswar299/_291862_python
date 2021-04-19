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

'''
The upper() method returns the string in upper case:
'''
a = "Hello, World!"
print(a.upper())

'''
The lower() method returns the string in lower case:
'''

a = "Hello, World!"
print(a.lower())

'''
The strip() method removes any whitespace from the beginning or the end:
'''

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

'''
The replace() method replaces a string with another string:
'''

a = "Hello, World!"
print(a.replace("H", "J"))

'''
The split() method splits the string into substrings if it finds instances of the separator:
'''

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

'''
To concatenate, or combine, two strings you can use the + operator.

Example
Merge variable a with variable b into variable c:
'''
a = "Hello"
b = "World"
c = a + b
print(c)

'''
To add a space between them, add a " ":
'''
a = "Hello"
b = "World"
c = a + " " + b
print(c)

'''
But we can combine strings and numbers by using the format() method!

The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

Example
Use the format() method to insert numbers into strings:
'''
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

'''
The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

Example
'''
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

'''
You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

Example
'''
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))



"""
String Methods
Python has a set of built-in methods that you can use on strings.

Note: All string methods returns new values. They do not change the original string.

Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""
