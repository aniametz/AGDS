import timeit
import operator
import create_graph as cg
from collections import OrderedDict


def print_time(function_name):
    timer = timeit.Timer(function_name, "from __main__ import " + function_name[:2])
    t = min(timer.repeat(10, 1))*1000
    print function_name + ": %fms" % (t, )

base_graph = [cg.irisG, cg.abaloneG]


def f1(i, attr, value):
    # obiekty o attr rownym val w i-tym grafie
    return base_graph[i][attr][value]


def f2(i, attr, value1, value2):
    # obiekty o attr miedzy value1 a value2 w i-tym grafie
    return [v for k, v in base_graph[i][attr].items() if value1 < k < value2]


def f3(i, attr, value):
    #obiekty o attr powyzej value w i-tym grafie
    return [v for k, v in base_graph[i][attr].items() if k > value]


def f4(i, attr, n):
    #n obiektow o max wartsociach attr w i-tym grafie
    chained = reduce(operator.add, [v for k, v in base_graph[i][attr].items()])
    return chained[-n:]


def f7(i, attr, n):
    s = sorted(base_graph[i][attr].items())
    print s
    arr = []
    for v in s:
        for i in v[1]:
            if len(arr) == n: break
            arr += i
    return arr


def f5(i, attr, record):
    #informacja o wartosci attr dla obiektu record
    for k, v in base_graph[i][attr].items():
        for i in v:
            if i == record:
                return k

def f6(i, attr1, value1, attr2, value2):
    # obiekty o wartosci attr1 powyzej value1 i wartosci attr2 ponizej value2
    chained1 = [v for k, v in base_graph[i][attr1].items() if k > value1]
    chained2 = [v for k, v in base_graph[i][attr2].items() if k < value2]
    return [v for v in chained1 if v in chained2]

'''
print_time("f1(0, 'sl', 5.0)")
print_time("f1(0, 'sw', 4.0)")
print_time("f1(0, 'pl', 1.5)")
print_time("f1(0, 'pw', 0.2)")
print "***"
print_time("f1(1, 'l', 0.38)")
print_time("f1(1, 'w', 0.887)")
print_time("f1(1, 'shell_w', 0.115)")
print_time("f1(1, 'ring', 9.0)")
print "***"
'''
'''
print_time("f2(0, 'sl', 5.0, 5.5)")
print_time("f2(0, 'sw', 3.5, 4.0)")
print_time("f2(0, 'pl', 1.3, 1.5)")
print_time("f2(0, 'pw', 0.2, 0.4)")
print "***"
'''
'''
print_time("f2(1, 'l', 0.38, 0.55)")
print_time("f2(1, 'w', 0.002, 0.0155)")
print_time("f2(1, 'shell_w', 0.115, 0.2)")
print_time("f2(1, 'ring', 9.0, 12)")
print "***"
'''
'''
print_time("f3(0, 'sl', 5.5)")
print_time("f3(0, 'sw', 4.0)")
print_time("f3(0, 'pl', 1.5)")
print_time("f3(0, 'pw', 0.4)")
print "***"
'''
'''
print_time("f3(1, 'l', 0.55)")
print_time("f3(1, 'w', 0.0155)")
print_time("f3(1, 'shell_w', 0.2)")
print_time("f3(1, 'ring', 9.0)")
print "***"
'''

print_time("f6(0, 'sl', 5.0, 'pl', 1.5)")
print_time("f6(0, 'sw', 4.0, 'pw', 0.4)")
print_time("f6(1, 'l', 0.55, 'w', 0.0155)")
print_time("f6(1, 'l', 0.38, 'd', 0.515)")

print list(cg.abaloneG["l"])[4]
print f7(1, 'l', 1)
