def sum(a,b,c):
    if a==b or b==c or c==a:
        sum=0;
    else:
        sum=(a+b+c)
    return sum
x,y,z=[int(a) for a in input("Enter three numbers:").split(",")]
print(sum(x,y,z))