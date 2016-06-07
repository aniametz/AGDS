import itertools
import timeit
import csv
import os
from numpy import *
from itertools import *
import sqlite3
from collections import defaultdict, OrderedDict
from operator import *
import create_graph as cg
import networkx as nx
import matplotlib as plt
from collections import namedtuple
import profile


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def read_data(filename):
    with open(os.path.join(APP_ROOT, filename)) as csvfile:
        data = [row for row in csv.reader(csvfile.read().splitlines())]
    return data


def print_time(function_name):
    timer = timeit.Timer(function_name, "from __main__ import abaloneG, w_nt, h_nt, " + function_name[:2])
    t = min(timer.repeat(100, 1))*10**6
    print function_name + ": " + "{:5.2f}".format(t) + " mikrosekund"

class Reference:
    def __init__(self, obj):
        self.obj = obj

    def get(self):
        return self.obj

    def set(self, obj):
        self.obj = obj


class Graph(object):

    def __init__(self):
        self._graph = {}
        self._type_dict = {"float": lambda x: float(x), "int": lambda x: int(x), "str": lambda x: str(x)}

    def add_edges(self, node, connections, column, type="str"):
        d = defaultdict(list)
        for i in range(len(connections)):
            r = str(i + 1)
            value = self._type_dict[type](connections[i][column])
            d[value].append(r)
        self._graph[node] = sorted(d.items())

    def add_attribute_nodes(self, node, connections, column, type="str"):
        nt = namedtuple(node, ["key", "value"])
        r = self.add_record_nodes(connections)
        d = defaultdict(set)
        for i in range(len(connections)):
            k = self._type_dict[type](connections[i][column])
            d[k].add(Reference(r.key[i]))
        d = OrderedDict(sorted(d.items()))
        return nt(key=d.keys(), value=d.values())

    def add_record_nodes(self, connections):
        r = []
        r += ["r"]
        r += [0] * len(connections)
        self._graph["r"] = r

    def __getitem__(self, node):
        return self._graph[node]

    def __iter__(self):
        return self._graph.iteritems()

    def __str__(self):
        return "{}".format(self._graph)


abaloneDATA = read_data("abalone.csv")
abaloneG = Graph()
abaloneG.add_edges("s", abaloneDATA, 0)
abaloneG.add_edges("l", abaloneDATA, 1, "float")
abaloneG.add_edges("d", abaloneDATA, 2, "float")
abaloneG.add_edges("h", abaloneDATA, 3, "float")
abaloneG.add_edges("w", abaloneDATA, 4, "float")



r = abaloneG.add_record_nodes(abaloneDATA)
print r

w_nt = abaloneG.add_attribute_nodes("w", abaloneDATA, 4, "float")
h_nt = abaloneG.add_attribute_nodes("h", abaloneDATA, 3, "float")

print w_nt.value
print h_nt.value


'''


def N3():
    return list(F1(w_nt.value[-10:]))[:10]

print N3()
print_time("N3()")


def N4():
    l = map(len, w_nt.value)
    value = max(l)
    i = l.index(value)
    return w_nt.key[i], value

print N4()
print_time("N4()")

def NT():
    start = w_nt.key.index(0.002)
    stop = w_nt.key.index(0.0735)
    return w_nt.value[start+1:stop-1]

print NT()
print_time("NT()")


abaloneDB = sqlite3.connect('abalone.db')
cursor = abaloneDB.cursor()

def f3():
    cursor.execute("SELECT id FROM abalone WHERE w > 0.002 and w < 0.0735")
    return cursor.fetchall()

def f4():
    cursor.execute("SELECT id FROM abalone WHERE w > 0.002 and w < 0.0735 and h > 0.01 and h < 0.135")
    return cursor.fetchall()

def f5():
    cursor.execute("SELECT id FROM abalone ORDER BY w DESC LIMIT 10")
    return cursor.fetchall()

def f7():
    cursor.execute("SELECT w, COUNT(w) AS counter FROM abalone "
                   "GROUP BY w ORDER BY counter DESC LIMIT 1")
    return cursor.fetchall()


print_time("f3()")
print_time("f4()")
print f5()
print_time("f5()")
print f7()
print_time("f7()")

abaloneDB.close()
'''

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
