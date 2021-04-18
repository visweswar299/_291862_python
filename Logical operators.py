print("""
Logical operators
""")

print("""
and
""")
print("""
Returns True if both statements are true
""")
x=7
print(x>3 and x<7)
print(x>3 and x<8)

print("""
or
""")
print("""
Returns True if one of the statements is true
""")
x=7
print(x>3 or x<7)
print(x>10 or x<0)

print("""
not
""")
print("""
Reverse the result, returns False if the result is true
""")
x=7
print(not(x>3 and x<8))
print(not(x>3 and x<7))