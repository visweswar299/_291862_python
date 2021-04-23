#write a program to check if the input number is
#-real numbers
#-float numbers
#-string
#-complex numbers
#-Zer0(0)

value=input("Enter the value:")
if(value>'0' and value.isnumeric()==True):
    print("Real number")
elif(value=='0'):
    print("Zero")

