from pandas import *
import matplotlib.pyplot as plt
import matplotlib

font = {'size': 16}
matplotlib.rc('font', **font)

df = DataFrame([[0.000467, 0.068580], [0.000467, 0.063915], [0.000467, 0.059250], [0.000467, 0.063915]],
                columns=['graf', 'tablica'])
df.plot.bar(color=['#CDDC39', '#2196F3'], rot=0)
plt.title('Filtracja 1 - Iris')
plt.xlabel('Operacja')
plt.ylabel('Czas [ms]')
plt.show()

plt.cla()
plt.clf()

df = DataFrame([[0.000467, 0.100304], [0.000467, 0.117566], [0.000467, 0.105436], [0.000467, 0.116166]],
               columns=['graf', 'tablica'])
df.plot.bar(color=['#CDDC39', '#2196F3'], rot=0)
plt.title('Filtracja 1 - Abalone')
plt.xlabel('Operacja')
plt.ylabel('Czas [ms]')
plt.show()

plt.cla()
plt.clf()

df = DataFrame([[0.005598, 0.082110], [0.004199, 0.071379], [0.006531, 0.061116], [0.003732, 0.079777]],
               columns=['graf', 'tablica'])
df.plot.bar(color=['#CDDC39', '#2196F3'], rot=0)
plt.legend(loc="upper right")
plt.title('Filtracja 2 - Iris')
plt.xlabel('Operacja')
plt.ylabel('Czas [ms]')
plt.show()

plt.cla()
plt.clf()

df = DataFrame([[0.021460, 1.885255], [0.334503, 1.209717], [0.127363, 1.753226], [0.004199, 1.402861]],
               columns=['graf', 'tablica'])
df.plot.bar(color=['#CDDC39', '#2196F3'], rot=0)
plt.title('Filtracja 2 - Abalone')
plt.xlabel('Operacja')
plt.ylabel('Czas [ms]')
plt.show()