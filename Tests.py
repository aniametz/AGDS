import time
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


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def read_data(filename):
    with open(os.path.join(APP_ROOT, filename)) as csvfile:
        data = [row for row in csv.reader(csvfile.read().splitlines())]
    return data


def print_time(function_name):
    timer = timeit.Timer(function_name, "from __main__ import abaloneG, " + function_name[:2])
    t = min(timer.repeat(10, 1))*10**6
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
        self._graph[node] = OrderedDict(sorted(d.items()))

    def has_key(self, node):
        return node in self._graph

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

print any(d["h"] == '0.002' for d in abaloneG)

G = nx.Graph()
G.add_nodes_from(["s", "l", "d", "h", "w", "r"])

G.clear()
for i in range(len(abaloneDATA)):
    r = str(i + 1)
    G.add_nodes_from(abaloneDATA[i][0])
    G.add_edge("s", abaloneDATA[i][0])

print G.number_of_nodes()
print G.number_of_edges()
print nx.degree(G)

nx.draw(G)

