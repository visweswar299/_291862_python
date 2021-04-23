#write  a pyhton program to convert a list into a nested dictionary
lis=[1,2,3,4,5]
dict=current={}
for num in lis:
    current[num]={}
    current=current[num]
print(dict)