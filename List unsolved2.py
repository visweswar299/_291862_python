#write a python program to change the position of every n-th value with the (n+1)th in a list

def change_position(list):
    for i in range(0,len(list)):
        list[i],list[i+1]=list[i+1],list[i]
    return list
list=[10,28,9,34,5,3,24]
print(change_position(list))