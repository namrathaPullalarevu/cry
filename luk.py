import pprint

import scipy

import scipy.linalg   # SciPy Linear Algebra Library

import numpy as np


a = np.matrix([ [1, 2, 3], [2, 3, 4], [1, 2, 5] ])

k = scipy.array([ [8, 2, 9], [4, 9, 4], [6, 7, 9] ])

print("Secret key is ")

print(k)

P, L, U = scipy.linalg.lu(k)


print "A:"

pprint.pprint(k)


print "P:"

pprint.pprint(P)


print "L:"

pprint.pprint(L)


print "U:"

pprint.pprint(U)



print(a)


ai = a.getI()

print "Inverse of a is:"

print(ai)

il = np.matmul(L,a)

print "Send product of L and D where L is Lower triangular matrix and D is agreed matrix"

print(il)

iu = np.matmul(U,a)

print "Send product of U and D where U is Upper triangular matrix and D is agreed matrix"

print(iu)

cl = np.matmul(il,ai)

cu = np.matmul(iu,ai)

print "Calculated L -Lower triangular matrix and U - Upper triangular matrix "

print(cl)

print(cu)

print "key exchanged is :"

key = np.matmul(cl,cu)

print(key)
