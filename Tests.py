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


def print_time(function_name):
    timer = timeit.Timer(function_name + "()", "from __main__ import " + function_name)
    t =  min(timer.repeat(10, 1))*1000
    print function_name + ": %fms" % (t, )


class Graph(object):

    def __init__(self):
        self._graph = {}

    def add_node(self, node):
        self._graph[node] = defaultdict(list)

    _typedict = {"float": lambda x: float(x), "int": lambda x: int(x), "str": lambda x: str(x)}

    def add_edges(self, node, connections, column, type="str"):
        if node not in self._graph:
            return None
        for i in range(len(connections)):
            r = str(i + 1)
            value = self._typedict[type](connections[i][column])
            self._graph[node][value].append(r)
        return self._graph[node].items()

    def __getitem__(self, node):
        return self._graph[node]

    def __iter__(self):
        return self._graph.iteritems()

    def __str__(self):
        return "{}".format(dict(self._graph))


abaloneDATA = read_data("abalone.csv")
abaloneG = Graph()
abaloneG.add_node("s")
abaloneG.add_edges("s", abaloneDATA, 0)
abaloneG.add_node("l")
abaloneG.add_edges("l", abaloneDATA, 1, "float")
abaloneG.add_node("d")
abaloneG.add_edges("d", abaloneDATA, 2, "float")
abaloneG.add_node("h")
abaloneG.add_edges("h", abaloneDATA, 3, "float")
abaloneG.add_node("w")
abaloneG.add_edges("w", abaloneDATA, 4, "float")


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




