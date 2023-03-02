from random import random
import numpy as np
import matplotlib.pyplot as plt

n = 10000
primeiro_quad = 0

# plt.ion()
plt.axhline(y=np.pi, xmin=0, xmax=1)
plt.title('Convergência a pi')
plt.xlabel("Passos")
plt.ylabel("Valor de pi calculado")

for i in range(1, n):
    x = random()
    y = random()

    if x**2 + y**2 <= 1:
        primeiro_quad += 1

        pi = 4*primeiro_quad/i

        plt.scatter(i, pi, c="black", s=1)

        # plt.draw()
        # plt.pause(0.01666)


pares_primeiroquad = primeiro_quad *100/n
plt.show()
print(f"pares no primeiro quadrante: {pares_primeiroquad}%, pi calculado: {pi}, erro absoluto = {abs(np.pi-pi)}")
