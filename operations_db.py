import timeit
from numpy import *
import sqlite3


def print_time(function_name):
    timer = timeit.Timer(function_name, "from __main__ import " + function_name[:2])
    t = min(timer.repeat(100, 1))*10**6
    return round(t, 3)
    # print function_name + ": " + "{:5.2f}".format(t) + " mikrosekund"


irisDB = sqlite3.connect('iris.db')
cursor = irisDB.cursor()


def f1(table, attr, value):
    # obiekty o wartosci attr rownej value z tabeli table
    cursor.execute("SELECT id FROM {} WHERE {} = ?".format(table, attr), (value, ))
    return cursor.fetchall()


def f2(table, attr, value1, value2):
    # obiekty o wartosci attr miedzy value1 a value2
    cursor.execute("SELECT id FROM {} WHERE {} > ? and {} < ?".format(table, attr, attr), (value1, value2))
    return cursor.fetchall()


def f3(table, attr, value):
    # obiekty o wartosci attr powyzej value
    cursor.execute("SELECT id FROM {} WHERE {} > ?".format(table, attr), (value, ))
    return cursor.fetchall()


def f4(table, attr, n):
    # n obiektow o max wartsociach attr
    cursor.execute("SELECT id FROM {} ORDER BY {} DESC LIMIT ?".format(table, attr), (n, ))
    return cursor.fetchall()


def f5(table, attr1, value1, attr2, value2):
    # obiekty o wartsoci attr1 powyzej value1 i attr2 ponizej value2
    cursor.execute("SELECT id FROM {} WHERE {} > ? and {} < ?".format(table, attr1, attr2), (value1, value2))
    return cursor.fetchall()


def f6(table, attr):
    # obiekty o najczesciej wsytepujacej wartosci attr
    cursor.execute("SELECT {}, COUNT({}) AS counter FROM {} "
                   "GROUP BY {} ORDER BY counter DESC LIMIT 1".format(attr, attr, table, attr))
    return cursor.fetchall()

def f8(table, attr):
    # obiekty calkowicie rozlaczne wzgledem jednego atrybutu
    cursor.execute("SELECT {} FROM {} ORDER BY {} DESC LIMIT 1".format(attr, table, attr))
    max = cursor.fetchall()
    max = max[0][0]
    cursor.execute("SELECT id FROM {} WHERE {} = ?".format(table, attr), (max,))
    smax = cursor.fetchall()
    cursor.execute("SELECT {} FROM {} ORDER BY {} ASC LIMIT 1".format(attr, table, attr))
    min = cursor.fetchall()
    min = min[0][0]
    cursor.execute("SELECT id FROM {} WHERE {} = ?".format(table, attr), (min,))
    smin = cursor.fetchall()
    return smin, smax


print_time("f2('iris', 'sl', 5.0, 5.5)")
print_time("f2('iris', 'sw', 3.5, 4.0)")
print_time("f2('iris', 'pl', 1.3, 1.5)")
print_time("f2('iris', 'pw', 0.2, 0.4)")
print_time("f5('iris', 'sl', 5.0, 'pl', 1.5)")
print_time("f5('iris', 'sw', 4.0, 'pw', 0.4)")

tf1_IRISDB = [print_time("f1('iris', 'sl', 5.0)"), print_time("f1('iris', 'sw', 4.0)"),
              print_time("f1('iris', 'pl', 1.5)"), print_time("f1('iris', 'pw', 5.0)")]

tf4_IRISDB = [print_time("f4('iris', 'sl', 10)"), print_time("f4('iris', 'sw', 10)"),
              print_time("f4('iris', 'pl', 10)"), print_time("f4('iris', 'pw', 10)")]

tf6_IRISDB = [print_time("f6('iris', 'sl')"), print_time("f6('iris', 'sw')"),
              print_time("f6('iris', 'pl')"), print_time("f6('iris', 'pw')")]

tf8_IRISDB = [print_time("f8('iris', 'sl')"), print_time("f8('iris', 'sw')"),
              print_time("f8('iris', 'pl')"), print_time("f8('iris', 'pw')")]

irisDB.close()

abaloneDB = sqlite3.connect('abalone.db')
cursor = abaloneDB.cursor()

print_time("f2('abalone', 'l', 0.38, 0.55)")
print_time("f2('abalone', 'w', 0.002, 0.0155)")
print_time("f2('abalone', 'shell_w', 0.115, 0.2)")
print_time("f2('abalone', 'ring', 9.0, 12)")
print_time("f5('abalone', 'l', 0.55, 'w', 0.0155)")
print_time("f5('abalone', 'shell_w', 0.2, 'ring', 9.0)")

tf1_ABADB = [print_time("f1('abalone', 'l', 0.38)"), print_time("f1('abalone', 'w', 0.887)"),
             print_time("f1('abalone', 'shell_w', 0.115)"), print_time("f1('abalone', 'ring', 9.0)")]

tf4_ABADB = [print_time("f4('abalone', 'l', 10)"), print_time("f4('abalone', 'd', 10)"),
              print_time("f4('abalone', 'h', 10)"), print_time("f4('abalone', 'w', 10)")]

tf6_ABADB = [print_time("f6('abalone', 'l')"), print_time("f6('abalone', 'd')"),
             print_time("f6('abalone', 'h')"), print_time("f6('abalone', 'w')")]

tf8_ABADB = [print_time("f8('abalone', 'l')"), print_time("f8('abalone', 'd')"),
             print_time("f8('abalone', 'h')"), print_time("f8('abalone', 'w')")]

