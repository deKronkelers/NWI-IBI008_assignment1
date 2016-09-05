# author: Hendrik Werner // s4549775
# author: Constantin Blach // s4329872
import numpy
from numpy import array, matrix

print("\n========== Assignment 1.1.1 ==========\n")

print("===== setup =====\n")

# assignment 1.1.1
x = array([6, 7, 8, 9, 10, 11, 12])
print("x = {}".format(x))

y = array([3, 7, 11, 15, 19, 23, 27])
print("y = {}".format(y))

w = array([1, 1, 0, 0.5, 1, 1.5, 2, 0, 0])
print("w = {}".format(w))

s = array([100, 98.8, 97.6, 96.4, 95.2])
print("s = {}".format(s))

z = array([.7, 1.0, 1.3, 1.6, 1.9, 2.2, 2.5, 2.8])
print("z = {}".format(z))

print("\n===== answers =====\n")

# assignment 1.1.1 a
v = 3 * x + y
print("v = 3x + y = {}".format(v))

# assignment 1.1.1 b
print("The dot product of x and y is {}".format(numpy.dot(x, y)))

# assignment 1.1.1 c

# assignment 1.1.1 d
z = z - 1
print("z = z - 1 = {}".format(z))

# assignment 1.1.1 e

# assignment 1.1.1 f
r = 2 * w - 5
print("r = 2w - 5 = {}".format(r))

print("\n========== Assignment 1.1.2 ==========\n")

print("===== setup =====\n")

# assignment 1.1.2
M = matrix("1 2 3; 6 8 4; 6 7 5")
print("M =\n{}".format(M))

N = matrix("4 6; 7 2; 5 1")
print("N =\n{}".format(N))

P = matrix("2 5; 5 5")
print("P =\n{}".format(P))

print("\n===== answers =====\n")

# assignment 1.1.2 a
A = M * N + N
print("A = MN + N =\n{}".format(A))

# assignment 1.1.2 b
B = numpy.transpose(N) * M
print("B = transpose(N) * M =\n{}".format(B))

# assignment 1.1.2 c
C = numpy.linalg.inv(P) + P
print("C = P^-1 + P =\n{}".format(C))

# assignment 1.1.2 d
try:
    print("AC (C + B) =\n{}".format(A * C * (C + B)))
except ValueError as e:
    print("AC (C + B) could not be computed: {}".format(e))

# assignment 1.1.2 e
