# author: Hendrik Werner // s4549775
# author: Constantin Blach // s4329872
import numpy
from numpy import matrix

# assignment 1.1.1
x = matrix("6 7 8 9 10 11 12")
print("x = {}".format(x))

y = matrix("3 7 11 15 19 23 27")
print("y = {}".format(y))

w = matrix("1 1 0 0.5 1 1.5 2 0 0")
print("w = {}".format(w))

s = matrix("100 98.8 97.6 96.4 95.2")
print("s = {}".format(s))

z = matrix(".7 1.0 1.3 1.6 1.9 2.2 2.5 2.8")
print("z = {}".format(z))

# assignment 1.1.1 a
v = 3 * x + y
print("v = {}".format(v))
