import time
import os
import csv
import sqlite3

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def read_data(filename):
    with open(os.path.join(APP_ROOT, filename)) as csvfile:
        data = [row for row in csv.reader(csvfile.read().splitlines())]
    return data


irisDB = sqlite3.connect('iris.db')  # 150 rekordow
irisC = irisDB.cursor()

irisC.execute("DROP TABLE iris")
irisC.execute("CREATE TABLE iris (id INTEGER PRIMARY KEY AUTOINCREMENT,"
              "sl REAL NOT NULL, sw REAL NOT NULL, pl NOT NULL, pw REAL NOT NULL,"
              "class TEXT NOT NULL)")

irisDATA = read_data("iris.csv")
del irisDATA[-1]
for i in irisDATA:
    irisC.execute("INSERT INTO iris VALUES (NULL, ?, ?, ?, ?, ?)", (float(i[0]), float(i[1]), float(i[2]), float(i[3]), i[4]))

irisDB.commit()

irisC.execute("SELECT * FROM iris")
print(irisC.fetchall())

irisDB.close()


aDB = sqlite3.connect('abalone.db')  # 4177 rekordow
aC = aDB.cursor()

aC.execute("DROP TABLE abalone")
aC.execute("CREATE TABLE abalone (id INTEGER PRIMARY KEY AUTOINCREMENT,"
              "s TEXT NOT NULL, l REAL NOT NULL, d REAL NOT NULL, h REAL NOT NULL,"
              "w REAL NOT NULL, shu_w REAL NOT NULL, vis_w REAL NOT NULL, shell_w REAL NOT NULL,"
              "ring INTEGER NOT NULL)")

aDATA = read_data("abalone.csv")
for i in aDATA:
    aC.execute("INSERT INTO abalone VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
               (i[0], float(i[1]), float(i[2]), float(i[3]), float(i[4]),
                float(i[5]), float(i[6]), float(i[7]), int(i[8])))

aDB.commit()

aC.execute("SELECT * FROM abalone")
print(aC.fetchall())

aDB.close()

