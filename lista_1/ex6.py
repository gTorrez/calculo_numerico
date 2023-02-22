from math import e, cos, sin, pi

l2 = 10
l1 = 8
gamma = (3*pi)/5

def f(x):
    return (l2 * (cos(pi - gamma - x) / sin(pi - gamma - x) ** 2)) - l1 * (cos(x) / sin(x) ** 2)


def derivada_fx(x, h=0.00001):
    return (f(x+h) - f(x))/h


def newton_raphson(x, tolerancia=10**(-12)):
    print("Método newton-raphson\n")
    i = 0
    xk_next = 0

    while abs(xk_next - x) > tolerancia:
        if i != 0:
            x = xk_next

        xk_next = x - f(x) / derivada_fx(x)

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


def calculaL(alfa):
    l = (l2/(sin(pi - gamma - alfa))) + (l1/sin(alfa))
    return l


alfa_newton = newton_raphson(1, 0.0000001)
print("===" * 20)
alfa_falsi = falsa_posicao(0.01, 1)
print("===" * 20)

l_newton = calculaL(alfa_newton)
print(f"Tamanho do L da barra por newton-raphson: {l_newton:.10f}")
l_falsi = calculaL(alfa_falsi)
print(f"Tamanho do L da barra por falsa-posição: {l_falsi:.10f}")
