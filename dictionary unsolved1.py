#write a program to merge two python dictionaries

d={1:'0',2:'3',3:'7'}
d1={4:'1',5:'8',6:'9'}
d2=d1.update(d)
print(d2) #prints None because updated into d1
print(d1)


def Merge(d,d1):
    res={**d, **d1}
    return res
d2 = Merge(d,d1)
print(d2)

