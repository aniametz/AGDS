from pandas import *
import matplotlib.pyplot as plt
import matplotlib

font = {'size': 16}
matplotlib.rc('font', **font)

data = [[1.40, 66.25], [1.87, 62.98], [1.40, 57.85], [1.40, 64.85]]
df = DataFrame(data, columns=['graf', 'tablica'])
df.plot.bar(color=['#CDDC39', '#2196F3'], rot=0)
plt.title('Iris I')
plt.xlabel('Operacja')
plt.ylabel('Czas [microsec]')
plt.show()

plt.cla()
plt.clf()

data = [[1.40, 416.61], [1.40, 420.81], [1.40, 390.49], [0.93, 426.41]]
df = DataFrame(data, columns=['graf', 'tablica'])
df.plot.bar(color=['#CDDC39', '#2196F3'], rot=0)
plt.title('Iris II')
plt.xlabel('Operacja')
plt.ylabel('Czas [microsec]')
plt.show()

plt.cla()
plt.clf()

df = DataFrame([[2.33, 921.87], [18.66, 1008.18], [4.20, 1078.62], [1.87, 1145.34 ]],
               columns=['graf', 'tablica'])
df.plot.bar(color=['#CDDC39', '#2196F3'], rot=0)
plt.title('Abalone I')
plt.xlabel('Operacja')
plt.ylabel('Czas [microsec]')
plt.show()

plt.cla()
plt.clf()


df = DataFrame([[16.80, 8585.58], [14.46, 8680.29], [8.40, 9038.12], [237.00, 10536.62]],
               columns=['graf', 'tablica'])
df.plot.bar(color=['#CDDC39', '#2196F3'], rot=0)
plt.title('Abalone II')
plt.xlabel('Operacja')
plt.ylabel('Czas [microsec]')
plt.show()

plt.cla()
plt.clf()