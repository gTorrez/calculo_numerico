from math import pi, cos


def f(x):
    return 2*x - cos(pi*x)


def falsa_posicao(a, b, tolerancia=10**(-12)):
    print("Método falsa posição\n")
    xk_list = []
    i = 0

    while True:
        xk = ((a*f(b))-(b*f(a)))/(f(b)-f(a))
        # mudar função

        if f(a)*f(xk) < 0:
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


falsa_posicao(-1, 1)
