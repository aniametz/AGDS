import timeit
from numpy import *
import sqlite3


def print_time(function_name):
    timer = timeit.Timer(function_name, "from __main__ import " + function_name[:2])
    t = min(timer.repeat(10, 1))*1000
    print function_name + ": %fms" % (t, )


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
    cursor.execute("SELECT id FROM [} ORDER BY {} DESC LIMIT ?".format(table, attr), (n, ))
    return cursor.fetchall()


def f5(table, attr, record):
    # informacja o wartosci attr dla obiektu record
    cursor.execute("SELECT {} FROM {} WHERE id = 1".format(attr, table), (record, ))
    return cursor.fetchall()


def f6(table, attr1, value1, attr2, value2):
    # obiekty o wartsoci attr1 powyzej value1 i attr2 ponizej value2
    cursor.execute("SELECT id FROM {} WHERE {} > ? and {} < ?".format(table, attr1, attr2), (value1, value2))
    return cursor.fetchall()

def f7(table, attr):
    # najczestsze wartosci attr
    cursor.execute("SELECT {}, COUNT({}) AS counter FROM {} "
                   "GROUP BY {} ORDER BY counter DESC LIMIT 1".format(attr, attr, table, attr))
    return cursor.fetchall()

'''
print_time("f1('iris', 'sepal_length', 5.0)")
print_time("f1('iris', 'sepal_width', 4.0)")
print_time("f1('iris', 'petal_length', 1.5)")
print_time("f1('iris', 'petal_width', 5.0)")
print "***"
print_time("f2('iris', 'sepal_length', 5.0, 5.5)")
print_time("f2('iris', 'sepal_width', 3.5, 4.0)")
print_time("f2('iris', 'petal_length', 1.3, 1.5)")
print_time("f2('iris', 'petal_width', 0.2, 0.4)")
'''
#f6(table, attr1, value1, attr2, value2)
print_time("f6('iris', 'sepal_length', 5.0, 'petal_length', 1.5)")
print_time("f6('iris', 'sepal_width', 4.0, 'petal_width', 0.4)")
print "***"

irisDB.close()

abaloneDB = sqlite3.connect('abalone.db')
cursor = abaloneDB.cursor()

'''
print "***"
print_time("f1('abalone', 'l', 0.38)")
print_time("f1('abalone', 'w', 0.887)")
print_time("f1('abalone', 'shell_w', 0.115)")
print_time("f1('abalone', 'ring', 9.0)")
print "***"
'''
'''
print_time("f2('abalone', 'l', 0.38, 0.55)")
print_time("f2('abalone', 'w', 0.002, 0.0155)")
print_time("f2('abalone', 'shell_w', 0.115, 0.2)")
print_time("f2('abalone', 'ring', 9.0, 12)")
print "***"
'''
#f6(table, attr1, value1, attr2, value2)
print_time("f6('abalone', 'l', 0.55, 'w', 0.0155)")
print_time("f6('abalone', 'shell_w', 0.2, 'ring', 9.0)")
print "***"

'''
#korelacja miedzy sl a sw w klasie setosa - numpy wykorzystane
#(Avg(X * Y) - Avg(X) * Avg(Y)) / (StDevP(X) * StDevP(Y))
start = time.clock()
irisC.execute("SELECT avg(sepal_length*sepal_width), avg(sepal_length), avg(sepal_width) FROM iris WHERE id < 50")
avg = irisC.fetchall()
irisC.execute("SELECT sepal_length FROM iris WHERE id < 50")
d1 = irisC.fetchall()
s1 = std(d1)
irisC.execute("SELECT sepal_width FROM iris WHERE id < 50")
d2 = irisC.fetchall()
s2 = std(d2)
#print (avg[0][0] - avg[0][1]*avg[0][2])/(s1*s2)
end = time.clock()
#print(end - start)

#selekcja podobnych wzorcow +/- 0.1
#rekord 1: 5.1,3.5,1.4,0.2,Iris-setosa
start = time.clock()
var = 0.1

res = []
for id in range(1, 151):
    irisC.execute("SELECT sepal_length, sepal_width, petal_length, sepal_width, class FROM iris WHERE id = ?", (id,))
    d = irisC.fetchall()
    irisC.execute("SELECT id, class FROM iris WHERE sepal_length < ? and sepal_length > ? "
                  "and sepal_width < ? and sepal_width > ? "
                  "and petal_length < ? and petal_length > ? "
                  "and sepal_width < ? and sepal_width > ?",
                  (d[0][0] + var, d[0][0] - var, d[0][1] + var, d[0][1] - var,
                   d[0][2] + var, d[0][2] - var, d[0][3] + var, d[0][3] - var))
    f = irisC.fetchall()
    if len(f) > 1:
        res += [f]
#print res
end = time.clock()
#print(end - start)

irisDB.close()

'''

