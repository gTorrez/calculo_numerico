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
    i = 0
    xk_next = 0

    while abs(xk_next-x) > tolerancia:
        if i != 0:
            x = xk_next

        valor_f = (l2*(cos(pi - gamma - x)/sin(pi - gamma - x)**2)) - l1*(cos(x)/sin(x)**2)
        valor_derivada_f = derivada(x)
        xk_next = x - valor_f/valor_derivada_f

        print(f"xk = {x:.10f}, f(xk) = {valor_f:.10f}, f'(xk) = {valor_derivada_f:.10f}, |xk+1 - xk| = {xk_next-x:.10f}")

        i += 1

    print(f"xk final = {xk_next:.10f}")
    return xk_next


def calculaL(alfa):
    L = (l2/(sin(pi - gamma - alfa))) + (l1/sin(alfa))
    print(f"Tamanho do L da barra: {L:.10f}")
    return L


alfa = newton_raphson(1, 0.0000001)
calculaL(alfa)
