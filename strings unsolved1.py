s = "restart"
char = 'r'
s1 = ''
length = len(s)
for i in range(length):
    if s[i] == char:
        s1 = s[0:i]+'$'+s[i+1:length]
print(s)
print(s1)
