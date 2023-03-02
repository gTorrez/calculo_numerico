import matplotlib.pyplot as plt  # biblioteca para plotar o gráfico
import numpy as np  # biblioteca para criar o intervalo


# definindo a função enunciada
def f(x):
   return 1*(x**7) - 7*(x**6) + 21*(x**5) - 35*(x**4) + 35*(x**3) - 21*(x**2) + 7*(x**1) - 1*(x**0)


# declarando os valores de borda do intervalo
xmin = 1 - 2/(10**8)
xmax = 1 + 2/(10**8)
x = np.linspace(xmin, xmax, 401) # criando o intervalo com 401 em um pontos equidistantes


# plotanto o gráfico
plt.plot(x, f(x), marker='', color='green')
plt.grid()
plt.show()


x = np.linspace(0, 2, 1000) # definindo um intervalo mais amplo
# plotanto o gráfico
plt.plot(x, f(x), color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('x**7 - 7*x**6 + 21*x**5 - 35*x**4  + 35*x**3 - 21*x**2 + 7*x - 1')
plt.grid(True)
plt.show()
