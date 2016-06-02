import time
import timeit
import csv
import os
from numpy import *
import sqlite3
from collections import defaultdict, OrderedDict
from operator import itemgetter
import create_graph as cg

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def read_data(filename):
    with open(os.path.join(APP_ROOT, filename)) as csvfile:
        data = [row for row in csv.reader(csvfile.read().splitlines())]
    return data


abaloneDATA = read_data("abalone.csv")
ring = defaultdict(list)
for i in range(len(abaloneDATA)):
    r = str(i + 1)
    ring[float(abaloneDATA[i][8])].append(r)

s = sorted(ring.items())
ring = OrderedDict(sorted(ring.items()))

#n obiektow o ring powyzej 9
start = time.clock()
arr = []
for v in s:
    if len(arr) == 5: break
    arr += v[1]
print arr
end = time.clock()
#print(end - start)



def f1():
    return ring[9]

def binary_search(list, item):
    first = 0
    last = len(list)-1
    found = False
    while first <= last and not found:
        middle = int((first + last)/2)
        if list[middle][0] == item:
            found = True
        else:
            if item < list[middle][0]:
                last = middle-1
            else:
                first = middle+1
    return list[middle][0]


def f2():
    return binary_search(s, 9)


def print_time(function_name):
    timer = timeit.Timer(function_name + "()", "from __main__ import " + function_name)
    t =  min(timer.repeat(10, 1))*1000
    print function_name + ": %fms" % (t, )

aDB = sqlite3.connect('abalone.db')
aC = aDB.cursor()

#najczestsze wartosci ring
start = time.clock()
aC.execute("SELECT ring, COUNT(ring) AS ringC FROM abalone GROUP BY ring ORDER BY ringC DESC LIMIT 1")
print(aC.fetchall())
end = time.clock()
print(end - start)

aDB.close()



