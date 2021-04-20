#car game
command=input("Type 'help' for options")
command1="help"
commandstart="start"
commandstop="stop"
commandquit="stop"
if command==command1:
    print("start- to start the car")
    print("stop - to stop the car")
    print("quit - to exit")
command2=input("What do you want to do?")
if command2==commandstart:
    print("Car started...ready to go")
elif command2==commandstop:
    print("car stopped")
elif command2==commandquit:
    print("Car stopped")
else:
    print("I can't understand")
command3=input("What do you wan to do next?")
if command2==commandstart:
    print("car is already started")
elif command2==commandstop:
    print("car stopped")
elif command2==commandquit:
    print("Car stopped")
