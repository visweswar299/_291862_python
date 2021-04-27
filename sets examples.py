# create set of integers
s = {1,2,3}
print(s)

# create mixed data types in set
s1 = {1,'viswa', 0.123, 'a', (1, 2, 3)}
print(s1)

# make set using list
s2 = set([1, 2, 3, 2])
print(s2)

# Distinguish set and dictionary while creating empty set

# initialize a with {}
a = {}

# check data type of a
print(type(a))

# initialize a with set()
a = set()

# check data type of a
print(type(a))

# initialize my_set
my_set = {1, 3}
print(my_set)

# my_set[0]
# if you uncomment the above line
# you will get an error
# TypeError: 'set' object does not support indexing

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2, 3, 4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4, 5], {1, 6, 8})
print(my_set)

# discard vs remove
s = {1, 2, 3, 4, 5, 6, 7}
print(s)
# discard method
s.discard(5)
print(s)
# discard of not available value in set
s.discard(5)
print(s)
# remove method
s.remove(3)
print(s)
# remove of not available value in set gives 'key error'
# print(s.remove(3))

