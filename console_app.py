from click import *
import os, inspect
import timeit
import sqlite3
import operations_db as db
import operations_graph as gr
import create_graph as cg

APP_ROOT = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
db_path = os.path.join(APP_ROOT, 'db_files')

# zmienne globalne do pomiaru czasu
g = Group()
d = None
a = ''
v = 0
a2 = ''
v2 = 0
c = None


def print_time(function_name):
    timer = timeit.Timer(function_name, "from __main__ import db, gr, d, a, v, a2, v2, c")
    t = min(timer.repeat(100, 1))*10**6
    print "Czas operacji: " + "{:5.2f}".format(t) + " mikrosekund"


def params():
    attributes = []
    d = []
    d.append(("Liczba rekordow", 1, 150))
    for node, nt in cg.irisG:
        if node not in ["cl", "r"]:
            d.append((node, nt.key[0], nt.key[-1]))
    attributes.append(d)
    d = []
    d.append(("Liczba rekordow", 1, 4177))
    for node, nt in cg.abaloneG:
        if node not in ["s", "r"]:
            d.append((node, nt.key[0], nt.key[-1]))
    attributes.append(d)
    return attributes


def find_key_dict(key, dict):
    if key in dict:
        return key
    else:
        key = min(dict.key, key=lambda k: abs(k - key))
        print "Wyszukiwanie dla najblizszego klucza w slowniku: " + str(key)
        return key


@g.command()
@option('--database', prompt="Wybierz baze danych: Iris [0] Abalone [1]", type=Choice(["0", "1"]))
@option('--function', prompt="Wybierz sposob przeszukiwania danych: 1 - 9", type=Choice(["1", "2", "3", "4", "5", "6",
                                                                                         "7", "8", "9"]))
def choose_function(database, function):
    global d
    d = int(database)
    p = params()
    echo("Dostepne atrybuty i ich przedzialy: " + str(p[d]))
    if function == "1":
        echo("Operacja 1. pozwala na wyswietlenie obiektow o wybranym atrybucie rownym wybranej wartosci.")
        function_1()
    if function == "2":
        echo("Operacja 2. pozwala na wyswietlenie obiektow o wartosciach wybranego atrybutu,"
             " ktore mieszcza sie w wybranym przedziale.")
        function_2()
    if function == "3":
        echo("Operacja 3. pozwala na wyswietlenie obiektow o wartosciach wybranego atrybutu,"
             " ktore sa powyzej wybranego progu.")
        function_3()
    if function == "4":
        echo("Operacja 4. pozwala na wyswietlenie wybranej liczby obiektow o maksymalnych wartosciach wybranego atrybutu. "
             "Potencjalne roznice w wynikach miedzy tabela a grafem spowodowane sa roznymi metodami sortowania rekordow.")
        function_4()
    if function == "5":
        echo("Operacja 5. pozwala na wyswietlenie obiektow o wartosciach atrybutu I powyzej wybranego progu I "
             "oraz o wartosciach atrybutu II ponizej wybranego progu II.")
        function_5()
    if function == "6":
        echo("Operacja 6. pozwala na wyswietlenie najczesciej powtarzajacej sie wartosci wybranego atrybutu wraz z obiektami,"
             " do ktorych jest przypisana.")
        function_6()
    if function == "7":
        echo("Operacja 7. pozwala na wyswietlenie obiektow o calkowitym podobienstwie do wybranego rekordu w bazie Iris "
             "lub o calkowitym podobienstwie do wybranego rekordu wzgledem atrybutow l, d, h w bazie Abalone.")
        function_7()
    if function == "8":
        echo("Operacja 8. pozwala na wyswietlenie obiektow calkowicie rozlacznych wzgledem jednego atrybutu.")
        function_8()
    if function == "9":
        echo(
            "Operacja 9. pozwala na wyswietlenie obiektow i stopnia czesciowego podobienstwa do wybranego rekordu "
            "wzgledem wszystkich atrybutow w bazie Iris (maksymalna waga: 4) lub wzgledem atrybutow l, d, h "
            "w bazie Abalone (maksymalna waga: 3).")
        function_9()

@g.command()
@option('--structure', prompt="Wybierz sposob przechowywania danych: graf [0] tablica [1]", type=Choice(["0", "1"]))
@option('--attr', prompt="Wybierz atrybut")
@option('--val', prompt="Wybierz wartosc")
def function_1(structure, attr, val):
    global a
    a = str(attr)
    try:
        gr.base_graph[d][a]
    except Exception:
        print "Nieprawidlowa nazwa atrybutu."
        function_1()
    global v
    try:
        v = float(val)
    except Exception:
        print "Nieprawidlowa wartosc."
        function_1()
    if structure == "0":
        v = find_key_dict(float(val), gr.base_graph[d][a])
        print "Szukane rekordy: ",
        print gr.f1(d, a, v)
        print_time("gr.f1(d, a, v)")
    else:
        db_name = db.base_table[d]+".db"
        DB = sqlite3.connect(os.path.join(db_path, db_name))
        global c
        c = DB.cursor()
        print "Szukane rekordy: ",
        print db.f1(d, c, a, v)
        print_time("db.f1(d, c, a, v)")
        DB.close()
    if confirm('Do you want to continue?'):
        choose_function()

@g.command()
@option('--structure', prompt="Wybierz sposob przechowywania danych: graf [0] tablica [1]", type=Choice(["0", "1"]))
@option('--attr', prompt="Wybierz atrybut")
@option('--val1', prompt="Wybierz wartosc I")
@option('--val2', prompt="Wybierz wartosc II wieksza od wartosci I")
def function_2(structure, attr, val1, val2):
    global a
    a = str(attr)
    try:
        gr.base_graph[d][a]
    except Exception:
        print "Nieprawidlowa nazwa atrybutu."
        function_2()
    global v, v2
    try:
        v = float(val1)
        v2 = float(val2)
    except Exception:
        print "Nieprawidlowa wartosc."
        function_2()
    if val1 >= val2:
        print "Wybrana wartosc II jest nieprawidlowa."
        function_2()
    if structure == "0":
        v = find_key_dict(float(val1), gr.base_graph[d][a])
        v2 = find_key_dict(float(val2), gr.base_graph[d][a])
        print "Szukane rekordy: ",
        print gr.f2(d, a, v, v2)
        print_time("gr.f2(d, a, v, v2)")
    else:
        db_name = db.base_table[d] + ".db"
        DB = sqlite3.connect(os.path.join(db_path, db_name))
        global c
        c = DB.cursor()
        print "Szukane rekordy: ",
        print db.f2(d, c, a, v, v2)
        print_time("db.f2(d, c, a, v, v2)")
        DB.close()
    if confirm('Do you want to continue?'):
        choose_function()

@g.command()
@option('--structure', prompt="Wybierz sposob przechowywania danych: graf [0] tablica [1]", type=Choice(["0", "1"]))
@option('--attr', prompt="Wybierz atrybut")
@option('--val', prompt="Wybierz wartosc progowa")
def function_3(structure, attr, val):
    global a
    a = str(attr)
    try:
        gr.base_graph[d][a]
    except Exception:
        print "Nieprawidlowa nazwa atrybutu."
        function_3()
    global v
    try:
        v = float(val)
    except Exception:
        print "Nieprawidlowa wartosc."
        function_3()
    if structure == "0":
        v = find_key_dict(float(val), gr.base_graph[d][a])
        print "Szukane rekordy: ",
        print gr.f3(d, a, v)
        print_time("gr.f3(d, a, v)")
    else:
        db_name = db.base_table[d] + ".db"
        DB = sqlite3.connect(os.path.join(db_path, db_name))
        global c
        c = DB.cursor()
        print "Szukane rekordy: ",
        print db.f3(d, c, a, v)
        print_time("db.f3(d, c, a, v)")
        DB.close()
    if confirm('Do you want to continue?'):
        choose_function()

@g.command()
@option('--structure', prompt="Wybierz sposob przechowywania danych: graf [0] tablica [1]", type=Choice(["0", "1"]))
@option('--attr', prompt="Wybierz atrybut")
@option('--n', prompt="Wybierz ilosc obiektow")
def function_4(structure, attr, n):
    global a
    a = str(attr)
    try:
        gr.base_graph[d][a]
    except Exception:
        print "Nieprawidlowa nazwa atrybutu."
        function_4()
    global v
    v = int(n)
    if structure == "0":
        print "Szukane rekordy: ",
        print gr.f4(d, a, v)
        print_time("gr.f4(d, a, v)")
    else:
        db_name = db.base_table[d] + ".db"
        DB = sqlite3.connect(os.path.join(db_path, db_name))
        global c
        c = DB.cursor()
        print "Szukane rekordy: ",
        print db.f4(d, c, a, v)
        print_time("db.f4(d, c, a, v)")
        DB.close()
    if confirm('Do you want to continue?'):
        choose_function()

@g.command()
@option('--structure', prompt="Wybierz sposob przechowywania danych: graf [0] tablica [1]", type=Choice(["0", "1"]))
@option('--attr1', prompt="Wybierz atrybut I")
@option('--val1', prompt="Wybierz wartosc progowa I")
@option('--attr2', prompt="Wybierz atrybut II")
@option('--val2', prompt="Wybierz wartosc progowa II")
def function_5(structure, attr1, val1, attr2, val2):
    global a, a2
    a = str(attr1)
    a2 = str(attr2)
    try:
        gr.base_graph[d][a]
        gr.base_graph[d][a2]
    except Exception:
        print "Nieprawidlowa nazwa atrybutu."
        function_5()
    global v, v2
    try:
        v = float(val1)
        v2 = float(val2)
    except Exception:
        print "Nieprawidlowa wartosc."
        function_5()
    if structure == "0":
        v = find_key_dict(float(val1), gr.base_graph[d][a])
        v2 = find_key_dict(float(val2), gr.base_graph[d][a2])
        print "Szukane rekordy: ",
        print gr.f5(d, a, v, a2, v2)
        print_time("gr.f5(d, a, v, a2, v2)")
    else:
        db_name = db.base_table[d] + ".db"
        DB = sqlite3.connect(os.path.join(db_path, db_name))
        global c
        c = DB.cursor()
        print "Szukane rekordy: ",
        print db.f5(d, c, a, v, a2, v2)
        print_time("db.f5(d, c, a, v, a2, v2)")
        DB.close()
    if confirm('Do you want to continue?'):
        choose_function()

@g.command()
@option('--structure', prompt="Wybierz sposob przechowywania danych: graf [0] tablica [1]", type=Choice(["0", "1"]))
@option('--attr', prompt="Wybierz atrybut")
def function_6(structure, attr):
    global a
    a = str(attr)
    try:
        gr.base_graph[d][a]
    except Exception:
        print "Nieprawidlowa nazwa atrybutu."
        function_6()
    if structure == "0":
        print "Szukane rekordy: ",
        print gr.f6(d, a)
        print_time("gr.f6(d, a)")
    else:
        db_name = db.base_table[d] + ".db"
        DB = sqlite3.connect(os.path.join(db_path, db_name))
        global c
        c = DB.cursor()
        print "Szukane rekordy: ",
        print db.f6(d, c, a)
        print_time("db.f6(d, c, a)")
        DB.close()
    if confirm('Do you want to continue?'):
        choose_function()


@g.command()
@option('--structure', prompt="Wybierz sposob przechowywania danych: graf [0] tablica [1]", type=Choice(["0", "1"]))
@option('--record', prompt="Wybierz rekord")
def function_7(structure, record):
    global v
    try:
        v = int(record)
        gr.fi(v)
        gr.fa(v)
    except Exception:
        print "Nieprawidlowa wartosc."
        function_7()
    if structure == "0":
        if d == "0":
            print "Szukane rekordy: ",
            print gr.fi(v)
            print_time("gr.fi(v)")
        else:
            print "Szukane rekordy: ",
            print gr.fa(v)
            print_time("gr.fa(v)")
    else:
        global c
        if d == "0":
            db_name = "iris.db"
            DB = sqlite3.connect(os.path.join(db_path, db_name))
            c = DB.cursor()
            print "Szukane rekordy: ",
            print db.fi(c, v)
            print_time("db.fi(c, v)")
            DB.close()
        else:
            db_name = "abalone.db"
            DB = sqlite3.connect(os.path.join(db_path, db_name))
            c = DB.cursor()
            print "Szukane rekordy: ",
            print db.fa(c, v)
            print_time("db.fa(c, v)")
            DB.close()
    if confirm('Do you want to continue?'):
        choose_function()

@g.command()
@option('--structure', prompt="Wybierz sposob przechowywania danych: graf [0] tablica [1]", type=Choice(["0", "1"]))
@option('--attr', prompt="Wybierz atrybut")
def function_8(structure, attr):
    global a
    a = str(attr)
    try:
        gr.base_graph[d][a]
    except Exception:
        print "Nieprawidlowa nazwa atrybutu."
        function_8()
    if structure == "0":
        print "Szukane rekordy: ",
        print gr.f8(d, a)
        print_time("gr.f8(d, a)")
    else:
        db_name = db.base_table[d] + ".db"
        DB = sqlite3.connect(os.path.join(db_path, db_name))
        global c
        c = DB.cursor()
        print "Szukane rekordy: ",
        print db.f8(d, c, a)
        print_time("db.f8(d, c, a)")
        DB.close()
    if confirm('Do you want to continue?'):
        choose_function()

@g.command()
@option('--record', prompt="Wybierz rekord")
def function_9(record):
    global v
    try:
        v = int(record)
        gr.ci(v)
        gr.ca(v)
    except Exception:
        print "Nieprawidlowa wartosc."
        function_9()
    if d == "0":
        print "Szukane rekordy: ",
        print gr.ci(v)
        print_time("gr.ci(v)")
    else:
        print "Szukane rekordy: ",
        print gr.ca(v)
        print_time("gr.ca(v)")
    if confirm('Do you want to continue?'):
        choose_function()


if __name__ == '__main__':
    echo("Aplikacja umozliwia porownanie czasu przeszukiwania tablicy oraz grafu.")
    choose_function()