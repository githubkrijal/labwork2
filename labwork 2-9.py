#check if given year is leap year or not

year=int(input("Enter the year"))
if year%4==0:
    print("It is a leap year")
else:
    print("It is a common year")