import array as arr
a=arr.array('i',[0,1,2,3,4,5,6,7,8,9,10,11])
print("Array before insertion:",end=" ")
for i in range(0,12):
	print(a[i],end=" ")
print()
a.append(15)
a.append(12)
a.append(10)
print("Array after insertion:",end=" ")
for i in range(0,15):
	print(a[i],end=" ")
print()