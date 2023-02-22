from random import random
import numpy as np
import matplotlib.pyplot as plt

n = 1000
primeiro_quad = 0

# plt.ion()
plt.axhline(y=np.pi, xmin=0, xmax=1)

for i in range(1, n):
    x = random()
    y = random()

    if x**2 + y**2 <= 1:
        primeiro_quad += 1

    pi = 4*primeiro_quad/i

    plt.scatter(i, pi, c="black", s=1)

    # plt.draw()
    # plt.pause(0.01666)

plt.show()
print(f"pi calculado: {pi}, erro absoluto = {abs(np.pi-pi)}")

# pi calculado: 3.140628125625125, erro = 0.0009645279646681715