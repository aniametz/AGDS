from collections import defaultdict, namedtuple
import inspect, os
import csv

APP_ROOT = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
path = os.path.join(APP_ROOT, 'csv_files')


def read_data(filename):
    with open(os.path.join(path, filename)) as csvfile:
        data = [row for row in csv.reader(csvfile.read().splitlines())]
    return data


class Graph(object):

    def __init__(self):
        self._graph = {}
        self._type_dict = {"float": lambda x: float(x), "int": lambda x: int(x), "str": lambda x: str(x)}

    def add_attribute_nodes(self, node, connections, column, type="str"):
        nt = namedtuple(node, ["key", "value"])
        d = defaultdict(list)
        dr = self._graph["r"]
        for i in range(len(connections)):
            k = self._type_dict[type](connections[i][column])
            d[k].append(i+1)
            dr[i+1].append(k)
        d = sorted(d.items())
        key = [i[0] for i in d]
        value = [i[1] for i in d]
        self._graph[node] = nt(key=key, value=value)
        self._graph["r"] = dr

    def add_record_nodes(self):
        self._graph["r"] = defaultdict(list)

    def get_nodes_number(self):
        l = 0
        for i in self._graph.items():
            for j in i:
                l += len(j)
        return l

    def __getitem__(self, node):
        return self._graph[node]

    def __iter__(self):
        return self._graph.iteritems()

    def __str__(self):
        return "{}".format(self._graph)


irisDATA = read_data("iris.csv")
del irisDATA[-1]

irisG = Graph()
irisG.add_record_nodes()
irisG.add_attribute_nodes("sl", irisDATA, 0, "float")
irisG.add_attribute_nodes("sw", irisDATA, 1, "float")
irisG.add_attribute_nodes("pl", irisDATA, 2, "float")
irisG.add_attribute_nodes("pw", irisDATA, 3, "float")
irisG.add_attribute_nodes("cl", irisDATA, 4)


abaloneDATA = read_data("abalone.csv")
abaloneG = Graph()
abaloneG.add_record_nodes()
abaloneG.add_attribute_nodes("s", abaloneDATA, 0)
abaloneG.add_attribute_nodes("l", abaloneDATA, 1, "float")
abaloneG.add_attribute_nodes("d", abaloneDATA, 2, "float")
abaloneG.add_attribute_nodes("h", abaloneDATA, 3, "float")
abaloneG.add_attribute_nodes("w", abaloneDATA, 4, "float")
abaloneG.add_attribute_nodes("shu_w", abaloneDATA, 5, "float")
abaloneG.add_attribute_nodes("vis_w", abaloneDATA, 6, "float")
abaloneG.add_attribute_nodes("shell_w", abaloneDATA, 7, "float")
abaloneG.add_attribute_nodes("ring", abaloneDATA, 8, "int")
