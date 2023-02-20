def calcula_raiz(a):
    n = 10
    x = 1

    for k in range(0, n):
        x = (x * (x**2 + (3 * a)))/((3 * x**2) + a)
    print(f"valor: {a}, raiz = {x:.8f}")


for i in range(1, 21):
    calcula_raiz(i)
