from numpy import *
from operator import *
from collections import namedtuple
import profile


r = namedtuple("r", ["key", "weight"])
R = r(key=[1, 2, 3, 4, 5, 6, 7, 8]*1000, weight=[0, 0, 0, 0, 0, 0, 0, 0]*1000)
a = namedtuple("r", ["key", "reference"])
A = a(key=[1.1, 1.2, 1.3, 1.4], reference=[[1, 7], [2, 8], [3, 4], [5, 6]])
B = a(key=[2.1, 2.4, 2.5], reference=[[1, 2, 7], [3, 6], [4, 5, 8]])

a1 = A.key[2]
r1 = A.key[-1] - A.key[0]
b2 = B.key[2]
r2 = B.key[-1] - B.key[0]

def FF():
    for i in range(len(A.key)):
     v = round(1 - abs(a1 - A.key[i])/r1, 2)
     for l in A.reference[i]:
         R.weight[l-1] += v

    for i in range(len(B.key)):
        v = round(1 - abs(b2 - B.key[i])/r2, 2)
        for l in B.reference[i]:
            R.weight[l-1] += v
    return R.weight

print R

profile.run("FF()")
print_time("FF()")
