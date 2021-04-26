# access characters

s = "Apple Juice"
# first character
print('s[0]=', s[0])
# Last character
print('s[-1=', s[-1])
# slicing 2nd to 5th character
print('s[1:5]=', s[1:5])
# slicing 6th to 2nd character
print('s[5:-2]=', s[5:-2])

# Concatenation of two strings
s = "Hello"
s1 = "World!"
print('s+s1=', s+s1)

# repeat the given string 5 times
s = "viswa"
print('s*5=', s*5)

# count no of 'l's in a string
count = 0
s = "Hello World!"
for i in range(len(s)):
    if(s[i] == 'l'):
        count += 1
print(count, 'letters found')


# find a and l in the given string
s = 'Hello World!'
print('a' in s)
print('l' in s)
print('a' not in s)
print('l' not in s)

# ignore escape sequence in given string
s = "This is \x61 \ngood example"
print(s)
# raw string to ignore escape sequences
s = r"This is \x61 \ngood example"
print(s)

# change lowercase to uppercase and vice versa
s = "Hello"
s1 = "hello"
print(s.lower())
print(s1.upper())

# replace hello with world
s = "Hello"
print(s.replace(s, 'World'))

# use split and join method to given string
s = 'This is python world'
print(s.split(' '))
s = ['This', 'is', 'python', 'world']
print(' '.join(s))

# find word in given string
s = 'This is python world'
print(s.find("is"))