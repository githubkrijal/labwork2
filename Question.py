pricehouse=1000000
credit=input("Is your credit good or not?'YES/NO':")
if credit=="YES":
    credit=True
if credit==True:
    print("You need to put down $",10/100*pricehouse)
else:
    print("You need to put down $",20/100*pricehouse)'