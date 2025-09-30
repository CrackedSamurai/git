import math
from unicodedata import numeric

class fraction():
    numerator = None
    denominator = None

def basic_num(numerator, denominator):
    div = math.gcd(int(numerator), int(denominator))
    numerator = numerator/div; denominator = denominator/div
    return int(numerator)

def basic_den(numerator, denominator):
    div = math.gcd(int(numerator), int(denominator))
    numerator = numerator/div; denominator = denominator/div
    return int(denominator)

def addition():
    denominator = math.lcm(f1.denominator, f2.denominator)
    numerator = (f1.numerator*denominator/f1.denominator)+(f2.numerator*denominator/f2.denominator)
    return f"{basic_num(numerator, denominator)}|{basic_den(numerator, denominator)}"

def multiplication():
    numerator = f1.numerator * f2.numerator
    denominator = f1.denominator * f2.denominator
    return f"{basic_num(numerator, denominator)}|{basic_den(numerator, denominator)}"

def subtraction():
    denominator = math.lcm(f1.denominator, f2.denominator)
    numerator = (f1.numerator*denominator/f1.denominator)-(f2.numerator*denominator/f2.denominator)
    return f"{basic_num(numerator, denominator)}|{basic_den(numerator, denominator)}"

def division():
    numerator = f1.numerator * f2.denominator
    denominator = f1.denominator * f2.numerator
    return f"{basic_num(numerator, denominator)}|{basic_den(numerator, denominator)}"

print("write fraction like this: x|y")
inp = input("=").replace(" ", "")
numeric_objects = ["+","-","*","/"]
for i in numeric_objects:
    if i in inp:
        operation = i
    inp = inp.replace(i, " ")
z1 = inp.split(" ")[0]
z2 = inp.split(" ")[1]
f1 = fraction(); f1.numerator = int(z1.split("|")[0]); f1.denominator = int(z1.split("|")[1])
f2 = fraction(); f2.numerator = int(z2.split("|")[0]); f2.denominator = int(z2.split("|")[1])

if operation == "+":
    print(addition())
elif operation == "*":
    print(multiplication())
elif operation == "-":
    print(subtraction())
elif operation == "/":
    print(division())