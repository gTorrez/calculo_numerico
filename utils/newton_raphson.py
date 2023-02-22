from math import e, cos

def f(x):
    return 4*cos(x) - e**(x)


def derivada_fx(x, h=0.00001):
    return (f(x+h)-f(x))/h


def newton_raphson(x, tolerancia=10**(-12)):
    print("Método newton-raphson\n")
    i = 0
    xk_next = 0

    while abs(xk_next-x) > tolerancia:
        if i != 0:
            x = xk_next

        xk_next = x - f(x)/derivada_fx(x)

        i += 1

    print(f"Número de iterações: {i}, Valor encontrado = {xk_next:.10f}")
    return xk_next


newton_raphson(0.1, 0.0000001)


