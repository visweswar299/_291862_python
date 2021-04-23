#write a python program to find repeated items in a tuple
t=(1,2,1,3,4,2,3,)
print(t)
for i in range(1,len(t)+1):
    print(t.count(i))
    
