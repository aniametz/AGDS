import timeit
from itertools import *
import create_graph as cg


def print_time(function_name):
    timer = timeit.Timer(function_name, "from __main__ import " + function_name[:2])
    t = min(timer.repeat(100, 1))*10**6
    print function_name + ": " + "{:5.2f}".format(t) + " mikrosekund"

base_graph = [cg.irisG, cg.abaloneG]


def ch(l):
    # zmiana listy list na liste
    return set(chain.from_iterable(l))


def f1(i, attr, value):
    # obiekty o attr rownym val w i-tym grafie
    start = base_graph[i][attr].key.index(value)
    return base_graph[i][attr].value[start]


def f2(i, attr, value1, value2):
    # obiekty o attr miedzy value1 a value2 w i-tym grafie
    start = base_graph[i][attr].key.index(value1)
    stop = base_graph[i][attr].key.index(value2)
    return base_graph[i][attr].value[start+1:stop-1]


def f3(i, attr, value):
    #obiekty o attr powyzej value w i-tym grafie
    start = base_graph[i][attr].key.index(value)
    return base_graph[i][attr].value[start+1:]


def f4(i, attr, n):
    #n obiektow o max wartsociach attr w i-tym grafie
    chained = list(ch(base_graph[i][attr].value[-n:]))
    return chained[:n]


def f5(i, attr1, value1, attr2, value2):
    # obiekty o wartosci attr1 powyzej value1 i wartosci attr2 ponizej value2
    start1 = base_graph[i][attr1].key.index(value1)
    d1 = base_graph[i][attr1].value[start1+1:]
    stop2 = base_graph[i][attr2].key.index(value2)
    d2 = base_graph[i][attr2].value[:stop2-1]
    return ch(d1) & ch(d2)


def f6(i, attr):
    # obiekty o najczesciej wsytepujacej wartosci attr
    l = map(len, base_graph[i][attr].value)
    k = l.index(max(l))
    return base_graph[i][attr].key[k], base_graph[i][attr].value[k]


def fa(record):
    # calkowite podobienstwo wzgledem l, d, h w grafie abalone
    r = cg.abaloneG["r"][record]
    v1 = cg.abaloneG["l"].key.index(r[1])
    v2 = cg.abaloneG["d"].key.index(r[2])
    v3 = cg.abaloneG["h"].key.index(r[3])
    return set(cg.abaloneG["l"].value[v1]) & set(cg.abaloneG["d"].value[v2]) & set(cg.abaloneG["h"].value[v3])


def fi(record):
    # obiekty o calkowitym podobienstwie wzgledem sl, pl w grafie iris
    r = cg.irisG["r"][record]
    v1 = cg.irisG["sl"].key.index(r[0])
    v2 = cg.irisG["pl"].key.index(r[2])
    return set(cg.irisG["sl"].value[v1]) & set(cg.irisG["pl"].value[v2])


def f8(i, attr):
    # obiekty calkowicie rozlaczne wzgledem jednego atrybutu
    return base_graph[i][attr].value[0], base_graph[i][attr].value[-1]


# print_time("f2(0, 'sl', 5.0, 5.5)")
# print_time("f2(0, 'sw', 3.5, 4.0)")
# print_time("f2(0, 'pl', 1.3, 1.5)")
# print_time("f2(0, 'pw', 0.2, 0.4)")
#
# print_time("f2(1, 'l', 0.38, 0.55)")
# print_time("f2(1, 'w', 0.002, 0.0155)")
# print_time("f2(1, 'shell_w', 0.115, 0.2)")
# print_time("f2(1, 'ring', 9.0, 12)")
#
# print_time("f3(0, 'sl', 5.5)")
# print_time("f3(0, 'sw', 4.0)")
# print_time("f3(0, 'pl', 1.5)")
# print_time("f3(0, 'pw', 0.4)")
#
# print_time("f3(1, 'l', 0.55)")
# print_time("f3(1, 'w', 0.0155)")
# print_time("f3(1, 'shell_w', 0.2)")
# print_time("f3(1, 'ring', 9.0)")

# print_time("f1(0, 'sl', 5.0)")
# print_time("f1(0, 'sw', 4.0)")
# print_time("f1(0, 'pl', 1.5)")
# print '***'
# print_time("f1(1, 'l', 0.38)")
# print_time("f1(1, 'w', 0.887)")
# print_time("f1(1, 'shell_w', 0.115)")
# print_time("f1(1, 'ring', 9.0)")
# print '***'
# print_time("f6(1, 'l')")
# print_time("f6(1, 'd')")
# print_time("f6(1, 'h')")
# print_time("f6(1, 'w')")
# print '***'
# print_time("f8(0, 'sl')")
# print_time("f8(0, 'sw')")
# print_time("f8(0, 'pl')")
# print_time("f8(0, 'pw')")



