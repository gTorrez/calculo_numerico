from math import pi, cos


def falsa_posicao(a, b, tolerancia=0.00000000001):
    print("Método falsa posição\n")
    xk_list = []
    i = 0

    while True:
        # mudar funções
        fa = 2*a - cos(pi*a)
        fb = 2*b - cos(pi*b)

        xk = ((a*fb)-(b*fa))/(fb-fa)
        # mudar função
        fxk = 2*xk - cos(pi*xk)

        if fa*fxk < 0:
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
