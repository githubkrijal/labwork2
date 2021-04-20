print("This program helps you find out if a number is positive negative or zero")
num1=int(input("Enter a number you want to check"))
if num1==0:
    print("The number is zero")
elif num1<0:
    print("The number is negative")
elif num1>0:
    print("The number is positive")
else:
    print("Number unable to recognize")