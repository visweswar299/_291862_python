#write python code that asks a user how many pizza slices they want. The pizzeria charges Rs. 123.00 a slice. if user order even
#number of slices, price per slice is rs 120.00. Print the total price depending on how many slices user orders.

print("If you order even no of pizza slices save Rs.3 per slice")
No_of_pizzas=int(input("Enter No of pizzas:"))
if(No_of_pizzas % 2 == 0):
    print("Total price is %d of your [no of pizzas] %d."%(No_of_pizzas*120,No_of_pizzas))
else:
    print("Total price is %d of your %d Pizza slices." % (No_of_pizzas * 123, No_of_pizzas))