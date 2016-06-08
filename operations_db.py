import timeit
from numpy import *
import sqlite3


def print_time(function_name):
    timer = timeit.Timer(function_name, "from __main__ import " + function_name[:2])
    t = min(timer.repeat(100, 1))*10**6
    print function_name + ": " + "{:5.2f}".format(t) + " mikrosekund"


irisDB = sqlite3.connect('iris.db')
cursor = irisDB.cursor()


def f1(table, attr, value):
    # obiekty o wartosci attr rownej value
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


def fi(record):
    # obiekty o calkowitym podobienstwie w grafie iris
    cursor.execute("SELECT sl, sw, pl, pw FROM iris WHERE id = ?", (record,))
    r = cursor.fetchall()
    cursor.execute("SELECT id FROM iris WHERE sl = ? AND sw = ? AND pl = ? AND pw = ?", (r[0][0], r[0][1], r[0][2], r[0][3]))
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

irisDB.close()

abaloneDB = sqlite3.connect('abalone.db')
cursor = abaloneDB.cursor()


def fa(record):
    # calkowite podobienstwo wzgledem l, d, h w grafie abalone
    cursor.execute("SELECT l, d, h FROM abalone WHERE id = ?", (record,))
    r = cursor.fetchall()
    cursor.execute("SELECT id FROM abalone WHERE l = ? AND d = ? AND h = ?", (r[0][0], r[0][1], r[0][2]))
    return cursor.fetchall()



