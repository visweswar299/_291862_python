print("""
Bitwise operators
""")

print("""
&(AND)
""")
print("""
Sets each bit to 1 if both bits are 1
""")
x=5
y=2
print(x&y)

print("""
|(OR)
""")
print("""
Sets each bit to 1 if one of two bits is 1
""")
x=5
y=2
print(x|y)

print("""
^(XOR)
""")
print("""
Sets each bit to 1 if only one of two bits is 1
""")
x=5
y=2
print(x^y)

print("""
~(NOT)
""")
print("""
Inverts all the bits
""")
x=5
y=2
print(~x)
print(~y)

print("""
<<(Zero fill left shift)
""")
print("""
Shift left by pushing zeros in from the right and let the leftmost bits fall off
""")
x=5
y=2
print(x<<y)

print("""
>>(Signed right shift)
""")
print("""
Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
""")
x=5
y=2
print(x>>y)