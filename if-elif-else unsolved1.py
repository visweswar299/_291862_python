#write a python program to get next day of the given date using if-elif-else

year=int(input("enter the year:"))
if year%400==0:
    leap_year=True
elif year%100==0:
    leap_year=False
elif year%4==0:
    leap_year=True
else:
    leap_year=False
month=int(input("Enter a month:"))
if month in (1,3,5,7,8,10,12):
    days=31
elif month==2:
    if leap_year:
        days=29
    else:
        days=28
else:
    days=30
day=int(input("Enter a day:"))
if day<days:
    day+=1
else:
    day=1
    if month==12:
        month=1
        year+=1
    else:
        month+=1
print("Next day is [y]-[m]-[d] %d-%d-%d."%(year,month,day))