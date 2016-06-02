from collections import defaultdict, OrderedDict
import os
import csv

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def read_data(filename):
    with open(os.path.join(APP_ROOT, filename)) as csvfile:
        data = [row for row in csv.reader(csvfile.read().splitlines())]
    return data


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

irisDATA = read_data("iris.csv")
del irisDATA[-1]

irisG = Graph()
irisG.add_node("sl")
irisG.add_edges("sl", irisDATA, 0, "float")
irisG.add_node("sw")
irisG.add_edges("sw", irisDATA, 1, "float")
irisG.add_node("pl")
irisG.add_edges("pl", irisDATA, 2, "float")
irisG.add_node("pw")
irisG.add_edges("pw", irisDATA, 3, "float")
irisG.add_node("class")
irisG.add_edges("class", irisDATA, 4)

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
abaloneG.add_node("shu_w")
abaloneG.add_edges("shu_w", abaloneDATA, 5, "float")
abaloneG.add_node("vis_w")
abaloneG.add_edges("vis_w", abaloneDATA, 6, "float")
abaloneG.add_node("shell_w")
abaloneG.add_edges("shell_w", abaloneDATA, 7, "float")
abaloneG.add_node("ring")
abaloneG.add_edges("ring", abaloneDATA, 8, "int")