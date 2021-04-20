name=input("What's your name")
name_cout=len(name)
if name_cout<3:
    print("Name must be at least 3 character")
elif name_cout>50:
    print("Name must be less than 50 character")
else:
    print("Your name looks good")