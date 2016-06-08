from operations_graph import *
from operations_db import *
from msvcrt import getch
import Tkinter as tk
import create_graph as cg

class MainApplication(tk.Frame):
    counter = 0
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=root.quit)

        text = tk.Text(root, background='#CFD8DC', foreground='#263238', font=('Tahoma', 12))
        info = "Bazy danych:\n\nIris - 150 rekordow, atrybuty:\n" \
               "sl: {}-{}, sw: {}-{}, pl: {}-{}, pw: {}-{}\n".format(cg.irisG["sl"].key[0], cg.irisG["sl"].key[-1],
                                                                     cg.irisG["sw"].key[0], cg.irisG["sw"].key[-1],
                                                                     cg.irisG["pl"].key[0], cg.irisG["pl"].key[-1],
                                                                     cg.irisG["pw"].key[0], cg.irisG["pw"].key[-1])
        info += "\nAbalone - 4177 rekordow, atrybuty:\n" \
                "l: {}-{}, d: {}-{}, h: {}-{}, w: {}-{},\nshu_w: {}-{}, vis_w: {}-{}, shell_w: {}-{}".format(
            cg.abaloneG["l"].key[0], cg.abaloneG["l"].key[-1], cg.abaloneG["d"].key[0], cg.abaloneG["d"].key[-1],
            cg.abaloneG["h"].key[0], cg.abaloneG["h"].key[-1], cg.abaloneG["w"].key[0], cg.abaloneG["w"].key[-1],
            cg.abaloneG["shu_w"].key[0], cg.abaloneG["shu_w"].key[-1], cg.abaloneG["vis_w"].key[0], cg.abaloneG["vis_w"].key[-1],
            cg.abaloneG["shell_w"].key[0], cg.abaloneG["shell_w"].key[-1])
        text.insert('1.0', info)
        text.insert('end', "\n\nWybierz strukture danych:\ng - graf, t - tablica\n")
        text.pack()

        root.bind('g', self.graph)
        root.bind('t', self.table)

    def graph(self, event):
        self.counter += 1
        t = tk.Toplevel(self)
        text = tk.Text(t, background='#CFD8DC', foreground='#263238', font=('Tahoma', 12))
        text.insert('end', "Grafy:\n0 - Iris, 1 - Abalone\n"
                           "Wybierz operacje:\n"
                           "1 - wybor obiektow o danej wartosci atrybutu\n"
                           "2 - wybor obiektow o wartosci atrybutu z danego przedzialu\n"
                           "3 - wybor obiektow wartosci atrybutu powyzej danej\n"
                           "4 - wybor n obiektow o max wartsociach atrybutu\n"
                           "5 - wybor obiektow o wartosci atrybutu powyzej wartosci 1 i wartosci atrybutu ponizej wartosci 2\n"
                           "6 - wybor obiektow o najczesciej wsytepujacej wartosci atrybutu\n"
                           "7 - wybor obiektow o calkowitej rozlacznosci wzgledem atrubutu\n")
        text.pack()
        t.bind('1', self.f1)
        t.bind('2', self.f2)

    def table(self, event):
        pass

    def f1(self, event):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()