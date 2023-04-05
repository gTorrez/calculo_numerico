import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from utils import calculaGaussSeidel, newton_raphson, is_caculable

# p(-1) = -32
# p(2) = 1
# p(4) = 3
# p(x) = c0 + c1(x + 1) + c2(x + 1)(x - 2)

# Dadas as condições iniciais, inicialmente devemos substituir estes valores na função p(x).
# Realizando esta substituição, temos o seguinte sistema:
#
#              -32 = 1c0 + 0c1 + 0c2     (1)
#               1 = 1c0 + 3c1 + 0c2      (2)
#               3 = 1c0 + 5c1 + 10c2     (3)
#
# Este sistema é de fácil resolução. Da eq. (1), temos que c0 é igual a -32. Substituindo este valor na eq. (2),
# temos que 32+1 = 3c1. Portanto, c1 = 11. Por fim, substituindo c0 e c1 na eq. (3), temos que c2 é igual a -2.
#
# Substituindo c0, c1 e c2 no polinimio p(x), temos que p(x) = -32 + 11(x + 1) -2(x + 1)(x - 2).
# Com este polinômio é possível plotar seu gráfico. Com o gráfico, podemos observar que, no intervalo analisado, há duas
# raízes, sendo elas: x1 = 1.813 e x2 = 4.686



def p(x, d=None, c0=sp.Symbol('c0'), c1=sp.Symbol('c1'), c2=sp.Symbol('c2')):

    px = c0 + c1*(x+1) + c2*(x+1)*(x-2)

    a = c0/c0
    b = (c1*(x+1))/c1
    c = (c2*(x+1)*(x-2))/c2

    print(f"p({x}) = {a}c0 + {b}c1 + {c}c2")
    return ([a, b, c], [d], px)


coefs_a = matriz = []
coefs_b = []

l1 = p(-1, -32)
l2 = p(2, 1)
l3 = p(4, 3)

matriz.append(l1[0])
matriz.append(l2[0])
matriz.append(l3[0])

coefs_b.append(l1[1])
coefs_b.append(l2[1])
coefs_b.append(l3[1])


if is_caculable(coefs_a, to_print=False):
    c0, c1, c2 = calculaGaussSeidel(coefs_a, coefs_b, graphic_on=False)
    print("=="*35)
    print(f"p(x) = {c0} + {c1}(x + 1) + {c2}(x + 1)(x - 2)")


    def f(x, c0, c1, c2):
        return c0 + c1*(x + 1) + c2*(x + 1)*(x - 2)

    raiz1 = newton_raphson(1)
    raiz2 = newton_raphson(4)

    x = np.linspace(0, 6.5)
    y = f(x, c0, c1, c2)
    plt.plot(x, y)
    plt.grid()
    plt.scatter(raiz1, 0, c='black', label=f"{raiz1:.2f}")
    plt.scatter(raiz2, 0, c='red', label=f"{raiz2:.2f}")
    plt.title(f"p(x) = {c0} + {c1}(x + 1) + {c2}(x + 1)(x - 2)")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.legend()
    plt.show()
