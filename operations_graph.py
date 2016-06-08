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


def fi(record):
    # obiekty o calkowitym podobienstwie w grafie iris
    r = cg.irisG["r"][record]
    v1 = cg.irisG["sl"].key.index(r[0])
    v2 = cg.irisG["sw"].key.index(r[1])
    v3 = cg.irisG["pl"].key.index(r[2])
    v4 = cg.irisG["pw"].key.index(r[3])
    return set(cg.irisG["sl"].value[v1]) & set(cg.irisG["sw"].value[v2]) \
           & set(cg.irisG["pl"].value[v3]) & set(cg.irisG["pw"].value[v4])


def fa(record):
    # calkowite podobienstwo wzgledem l, d, h w grafie abalone
    r = cg.abaloneG["r"][record]
    v1 = cg.abaloneG["l"].key.index(r[1])
    v2 = cg.abaloneG["d"].key.index(r[2])
    v3 = cg.abaloneG["h"].key.index(r[3])
    return set(cg.abaloneG["l"].value[v1]) & set(cg.abaloneG["d"].value[v2]) & set(cg.abaloneG["h"].value[v3])


def f8(i, attr):
    # obiekty calkowicie rozlaczne wzgledem jednego atrybutu
    return base_graph[i][attr].value[0], base_graph[i][attr].value[-1]


def ci(record):
    # czesciowe podobienstwo obiektow o sasiedniej wartosci wszystkich atrybutow do obiektu record
    d = []
    r = cg.irisG["r"][record]
    l = [(cg.irisG["sl"], cg.irisG["sl"].key.index(r[0])), (cg.irisG["sw"], cg.irisG["sw"].key.index(r[1])),
         (cg.irisG["pl"], cg.irisG["pl"].key.index(r[2])), (cg.irisG["pw"], cg.irisG["pw"].key.index(r[3]))]
    for i, k in l:
        tmp = k + 1
        try:
            i.key[tmp]
        except IndexError:
            tmp = k - 1
        a1 = i.key[tmp]
        r1 = i.key[-1] - i.key[0]
        v1 = round(1 - abs(a1 - i.key[k]) / r1, 2)
        d1 = {item: v1 for item in i.value[tmp]}
        d.append(d1)
    D = {k: d[0].get(k, 0) + d[1].get(k, 0) + d[2].get(k, 0) + d[3].get(k, 0)
          for k in set(d[0]) | set(d[1]) | set(d[2]) | set(d[3])}
    return D


def ca(record):
    # czesciowe podobienstwo obiektow o sasiedniej wartosci atrybutow l, d, h do obiektu record
    d = []
    r = cg.abaloneG["r"][record]
    l = [(cg.abaloneG["l"], cg.abaloneG["l"].key.index(r[1])), (cg.abaloneG["d"], cg.abaloneG["d"].key.index(r[2])),
         (cg.abaloneG["h"], cg.abaloneG["h"].key.index(r[3]))]
    for i, k in l:
        tmp = k - 1
        try:
            i.key[tmp]
        except IndexError:
            tmp = k + 1
        a1 = i.key[tmp]
        r1 = i.key[-1] - i.key[0]
        v1 = round(1 - abs(a1 - i.key[k]) / r1, 2)
        d1 = {item: v1 for item in i.value[tmp]}
        d.append(d1)
    D = {k: d[0].get(k, 0) + d[1].get(k, 0) + d[2].get(k, 0)
          for k in set(d[0]) | set(d[1]) | set(d[2])}
    return D

#sorted(D.items(), key=itemgetter(1), reverse=True)





