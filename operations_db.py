
base_table = ["iris", "abalone"]


def f1(i, cursor, attr, value):
    # obiekty o wartosci attr rownej value
    cursor.execute("SELECT id FROM {} WHERE {} = ?".format(base_table[i], attr), (value, ))
    return cursor.fetchall()


def f2(i, cursor, attr, value1, value2):
    # obiekty o wartosci attr miedzy value1 a value2
    cursor.execute("SELECT id FROM {} WHERE {} > ? and {} < ?".format(base_table[i], attr, attr), (value1, value2))
    return cursor.fetchall()


def f3(i, cursor, attr, value):
    # obiekty o wartosci attr powyzej value
    cursor.execute("SELECT id FROM {} WHERE {} > ?".format(base_table[i], attr), (value, ))
    return cursor.fetchall()


def f4(i, cursor, attr, n):
    # n obiektow o max wartsociach attr
    cursor.execute("SELECT id FROM {} ORDER BY {} DESC LIMIT ?".format(base_table[i], attr), (n, ))
    return cursor.fetchall()


def f5(i, cursor, attr1, value1, attr2, value2):
    # obiekty o wartsoci attr1 powyzej value1 i attr2 ponizej value2
    cursor.execute("SELECT id FROM {} WHERE {} > ? and {} < ?".format(base_table[i], attr1, attr2), (value1, value2))
    return cursor.fetchall()


def f6(i, cursor, attr):
    # obiekty o najczesciej wsytepujacej wartosci attr
    cursor.execute("SELECT {} AS counter FROM {} "
                   "GROUP BY {} ORDER BY COUNT({}) DESC LIMIT 1".format(attr, base_table[i], attr, attr))
    value = cursor.fetchall()
    value = value[0][0]
    cursor.execute("SELECT id FROM {} WHERE {} = ?".format(base_table[i], attr), (value, ))
    return (value,  cursor.fetchall())


def fi(cursor, record):
    # obiekty o calkowitym podobienstwie w grafie iris
    cursor.execute("SELECT sl, sw, pl, pw FROM iris WHERE id = ?", (record,))
    r = cursor.fetchall()
    cursor.execute("SELECT id FROM iris WHERE sl = ? AND sw = ? AND pl = ? AND pw = ?", (r[0][0], r[0][1], r[0][2], r[0][3]))
    return cursor.fetchall()


def fa(cursor, record):
    # calkowite podobienstwo wzgledem l, d, h w grafie abalone
    cursor.execute("SELECT l, d, h FROM abalone WHERE id = ?", (record,))
    r = cursor.fetchall()
    cursor.execute("SELECT id FROM abalone WHERE l = ? AND d = ? AND h = ?", (r[0][0], r[0][1], r[0][2]))
    return cursor.fetchall()


def f8(i, cursor, attr):
    # obiekty calkowicie rozlaczne wzgledem jednego atrybutu
    cursor.execute("SELECT {} FROM {} ORDER BY {} DESC LIMIT 1".format(attr, base_table[i], attr))
    max = cursor.fetchall()
    max = max[0][0]
    cursor.execute("SELECT id FROM {} WHERE {} = ?".format(base_table[i], attr), (max,))
    smax = cursor.fetchall()
    cursor.execute("SELECT {} FROM {} ORDER BY {} ASC LIMIT 1".format(attr, base_table[i], attr))
    min = cursor.fetchall()
    min = min[0][0]
    cursor.execute("SELECT id FROM {} WHERE {} = ?".format(base_table[i], attr), (min,))
    smin = cursor.fetchall()
    return smin, smax



