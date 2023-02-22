r = 0.401
s = 42.7*(10**(-6))
n_molec = 1000
t = 300
p = 3.5*(10**7)
k = 1.3806503 * (10**(-23))

tol = 10**(-12)


def f(x):
    return (p + r * (n_molec / x) ** 2) * (x - n_molec * s) * (1 / (k * n_molec * t))


def biseccao(a, b, tolerancia=10**(-12)):
    i = 0

    print("Método da bissecção\n")
    while abs(b-a)/2 > tolerancia:
        if f(a)*f(b) >= 0 and i == 0:
            print("Intervalo inválido pois não satisfaz f(a)f(b) < 0")
            return

        m = (a+b)/2

        if f(a)*f(m) < 0:
            a = a
            b = m
        else:
            a = m
            b = b

        i += 1

    print(f"Número de iterações: {i}, Valor encontrado = {m:.10f}")


biseccao(0.00001, 1, tol)
