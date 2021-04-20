#weigth converter
weight=int(input("Enter your weight"))
weightconfirm=input("Is it in kg or lbs")

if weightconfirm=='kg':
    weightconfirm=True
    if weightconfirm==True:
        weightconfirm=float(weight/0.5)
    print("Your weight in lbs is",weightconfirm)

elif weightconfirm=='lbs':
    weightconfirm=True
    if weightconfirm==True:
        weightconfirm=float(weight*0.5)
    print("Your weight in lbs is",weightconfirm)

else:
    print("invalid character detected")



