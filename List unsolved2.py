#write a python program to change the position of every n-th value with the (n+1)th in a list

l=[1,2,3,4,5,6]
for i in range(0,len(l),2):
    if i<len(l):
        l[i],l[i+1]=l[i+1],l[i]
print(l)