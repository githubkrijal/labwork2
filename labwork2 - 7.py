#given a positive number, print its fractional part
import math
num=float(input("Enter a fractional number"))
fraction=math.modf(num)
print(fraction)