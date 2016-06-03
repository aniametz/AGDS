import itertools
import timeit
import csv
import os
from numpy import *
import sqlite3
from collections import defaultdict, OrderedDict
from operator import *
import create_graph as cg
import networkx as nx
import matplotlib as plt
import bisect
from collections import namedtuple


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def read_data(filename):
    with open(os.path.join(APP_ROOT, filename)) as csvfile:
        data = [row for row in csv.reader(csvfile.read().splitlines())]
    return data


def print_time(function_name):
    timer = timeit.Timer(function_name, "from __main__ import abaloneG, " + function_name[:2])
    t = min(timer.repeat(100, 1))*10**6
    print function_name + ": " + "{:5.2f}".format(t) + " mikrosekund"


class Graph(object):

    def __init__(self):
        self._graph = {}
        self._typedict = {"float": lambda x: float(x), "int": lambda x: int(x), "str": lambda x: str(x)}

    def add_edges(self, node, connections, column, type="str"):
        d = defaultdict(list)
        for i in range(len(connections)):
            r = str(i + 1)
            value = self._typedict[type](connections[i][column])
            d[value].append(r)
        self._graph[node] = sorted(d.items())

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
abaloneG.add_edges("r", abaloneDATA, 0)

print abaloneG["w"]

'''
def FF():
    start = abaloneG["w"].keys().index(0.002)
    stop = abaloneG["w"].keys().index(0.038)
    return list(itertools.islice(abaloneG["h"].values(), start, stop))

print FF()
print_time("FF()")

    keys = zip(*abaloneG["w"])[0]
    values = zip(*abaloneG["w"])[1]
    start = keys.index(0.002)
    stop = keys.index(0.0735)
'''

def F2():
    return [v for k, v in abaloneG["w"][0:74]]

print F2()
print_time("F2()")

def Bi():
    stop = bisect.bisect_left([k for k, v in abaloneG["w"]], 0.002)
    start = bisect.bisect_left([k for k, v in abaloneG["w"]], 0.0735)
    return start, stop

print_time("Bi()")


def f2():
    return [v for k, v in abaloneG["w"] if 0.002 < k < 0.0735]

print f2()
print_time("f2()")

abaloneDB = sqlite3.connect('abalone.db')
cursor = abaloneDB.cursor()


def f3():
    cursor.execute("SELECT id FROM abalone WHERE w > 0.002 and w < 0.0735")
    return cursor.fetchall()

print f3()
print_time("f3()")

abaloneDB.close()

def add_nt(node, data):
    nt = namedtuple(node, ["key", "value"])
    d = defaultdict(list)
    for i in range(len(data)):
        r = str(i + 1)
        d[str(data[i])].append(r)
    return nt(key=d.keys(), value=d.values())

d = [1, 2, 3, 1, 1, 2, 2, 1, 3, 4, 5, 6, 1, 1]
e = add("w", d)

def NT():
    if e.key > 2:
        return e.value
    return None

print_time("NT()")



