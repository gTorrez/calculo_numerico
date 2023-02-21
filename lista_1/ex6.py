from math import e, cos, sin, pi

l2 = 10
l1 = 8
gamma = (3*pi)/5


def derivada(x, h=0.00001):
    fx = (l2*(cos(pi - gamma - x)/sin(pi - gamma - x)**2)) - l1*(cos(x)/sin(x)**2)
    fxh = (l2*(cos(pi - gamma - (x+h))/sin(pi - gamma - (x+h))**2)) - l1*(cos(x+h)/sin(x+h)**2)
    resultado = (fxh-fx)/h
    return resultado


def newton_raphson(x, tolerancia):
    print("Método newton-raphson\n")
    i = 0
    xk_next = 0

    while abs(xk_next-x) > tolerancia:
        if i != 0:
            x = xk_next

        valor_f = (l2*(cos(pi - gamma - x)/sin(pi - gamma - x)**2)) - l1*(cos(x)/sin(x)**2)
        valor_derivada_f = derivada(x)
        xk_next = x - valor_f/valor_derivada_f

        # print(f"xk = {x:.10f}, f(xk) = {valor_f:.10f}, f'(xk) = {valor_derivada_f:.10f}, |xk+1 - xk| = {xk_next-x:.10f}")

        i += 1

    print(f"Número de iterações: {i}, Valor encontrado = {xk_next:.10f}")
    return xk_next


def falsa_posicao(a, b, tolerancia=0.00000000001):
    print("Método falsa posição\n")
    xk_list = []
    i = 0

    while True:
        fa = (l2*(cos(pi - gamma - a)/sin(pi - gamma - a)**2)) - l1*(cos(a)/sin(a)**2)
        fb = (l2*(cos(pi - gamma - b)/sin(pi - gamma - b)**2)) - l1*(cos(b)/sin(b)**2)

        xk = ((a * fb) - (b * fa)) / (fb - fa)
        fxk = (l2*(cos(pi - gamma - xk)/sin(pi - gamma - xk)**2)) - l1*(cos(xk)/sin(xk)**2)

        if fa * fxk < 0:
            a = a
            b = xk
        else:
            a = xk
            b = b

        xk_list.append(xk)
        if len(xk_list) > 2:
            xk_list.pop(0)

        if (len(xk_list) == 2) and abs(xk_list[1] - xk_list[0]) <= tolerancia:
            print(f"Número de iterações: {i}, Valor encontrado: {xk:.10f}")
            break

        i += 1

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
