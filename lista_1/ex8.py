r = 0.401
s = 42.7*(10**(-6))
n_molec = 1000
t = 300
p = 3.5*(10**7)
k = 1.3806503 * (10**(-23))

tol = 10**(-12)


def f(x):
    return (p + r * (n_molec/x)**2)*(x-n_molec*s)*(1/(k*n_molec*t))


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


def falsa_posicao(a, b, tolerancia=10**(-12)):
    print("Método falsa posição\n")
    xk_list = []
    i = 0

    while True:
        xk = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))
        # mudar função

        if f(a) * f(xk) < 0:
            a = a
            b = xk
        else:
            a = xk
            b = b

        xk_list.append(xk)
        if len(xk_list) > 2:
            xk_list.pop(0)

        if (len(xk_list) == 2) and abs(xk_list[1] - xk_list[0]) <= tolerancia:
            break

        i += 1

    print(f"Número de iterações: {i}, Valor encontrado: {xk:.10f}")
    return xk


biseccao(-1.0, 1000.0, tol)
print("=="*30)
falsa_posicao(0.01, 20, tol)
print("=="*30)
newton_raphson(0.01, tol)
print("=="*30)
