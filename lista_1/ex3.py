from math import e

n = 0

i_n = (e - 1) / e
while n <= 180:
    i_n = 1 - ((n + 1)*i_n)
    n += 1
    print(i_n)
