from math import e, cos


def derivada(x, h=0.00001):
    fx = 4*cos(x) - e**(x)
    fxh = 4*cos(x+h) - e**(x+h)
    resultado = (fxh-fx)/h
    return resultado


def newton_raphson(xk, tolerancia):
    i = 0
    xk_next = 0

    while abs(xk_next-xk) > tolerancia:
        if i != 0:
            xk = xk_next

        valor_f = 4*cos(xk) - e**xk
        valor_derivada_f = derivada(xk)
        xk_next = xk - valor_f/valor_derivada_f

        print(f"xk = {xk:.10f}, f(xk) = {valor_f:.10f}, f'(xk) = {valor_derivada_f:.10f}, |xk+1 - xk| = {xk_next-xk:.10f}")

        i += 1

    print(f"xk final = {xk_next:.10f}")


newton_raphson(0.1, 0.0000001)


