import math
import sys
import turtle
print("usage: python3 degrees.py numberofmovements# rad|deg lengthofmovement# anglemod#")
t = turtle.Turtle()
b = []
for i in range(int(sys.argv[1])):
    b.append(i)

if sys.argv[2] == "deg":
    W = lambda x:  print(str(t.forward(x % 10 + int(sys.argv[3]))) + str(t.left(math.degrees(x) % int(sys.argv[4]) + int(sys.argv[3])))) #+ "number " + str(x) + "\r\n" + str(math.degrees(x)) + " Degrees" + "\r\n"  + str(math.radians(x)) + " Radians" + "\r\n" + str(math.sinh(x)) + " Hyperbolic Sines" + "\r\n" + str(math.asinh(x)) + " Inverse Hyperbolic Sines" + "\r\n")
if sys.argv[2] == "rad":
    W = lambda x:  print(str(t.forward(x % 10 + int(sys.argv[3]))) + str(t.right(math.radians(x) % int(sys.argv[4]) + int(sys.argv[3]))))
print(list(map(W, b)))
