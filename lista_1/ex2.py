import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 1*(x**7) - 7*(x**6) + 21*(x**5) - 35*(x**4) + 35*(x**3) - 21*(x**2) + 7*(x**1) - 1*(x**0)


xmin = 1 - 2/(10**8)
xmax = 1 + 2/(10**8)

x = np.linspace(xmin, xmax, 401)
plt.plot(x, f(x), marker='', color='green')
plt.grid()
plt.show()
