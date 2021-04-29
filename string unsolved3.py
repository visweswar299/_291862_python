s = 'restart'
char = 'r'
length = len(s)
count = 0
for i in range(length):
    if s[i] == char:
        count += 1
print(count)
