import matplotlib.pyplot as plt
from math import e, cos


def divideCoeficiente(coefs_a, coefs_b):
    divisores = []

    for i in range(0, len(coefs_a)):
        for j in range(0, len(coefs_a[i])):
            if i == j:
                divisor = coefs_a[i][j]
                divisores.append(divisor)
                break

        for k in range(0, len(coefs_a[i])):
            coefs_a[i][k] = coefs_a[i][k]/abs(divisores[i])

        for m in range(0, len(coefs_b[i])):
            coefs_b[i][m] = coefs_b[i][m]/abs(divisores[i])

    print("===Nova matriz===")
    for n in range(0, len(coefs_a)):
        print(f"{coefs_a[n]} {coefs_b[n]}")

    print("=="*35)


def checaCriterioLinha(coefs_a, to_print=True):
    somas = []
    soma = 0

    for i in range(0, len(coefs_a)):
        for j in range(0, len(coefs_a[i])):
            if i != j:
                soma += abs(coefs_a[i][j])

        somas.append(float(f"{soma:.2f}"))
        soma = 0

    if to_print:
        print("Critério de soma por linhas\n")
        print(somas)
    if max(somas) < 1:
        if to_print:
            print(f"{max(somas)} < 1 \nLogo, converge")
            print("="*35)

        return True
    else:
        if to_print:
            print(f"{max(somas)} >= 1 \nLogo, não converge")
            print("=="*35)

        return False


def checaCriterioSassenfeld(coefs_a, to_print=True):
    b1 = 0
    b2 = 0
    b3 = 0

    for i in range(0, len(coefs_a)):
        if i == 0:
            b1 = abs(coefs_a[i][1]) + abs(coefs_a[i][2])
        elif i == 1:
            b2 = abs(coefs_a[i][0]) * b1 + abs(coefs_a[i][2])
        else:
            b3 = abs(coefs_a[i][0]) * b1 + abs(coefs_a[i][1]) * b2
    if to_print:
        print("Critério de Sassenfeld\n")
        print(f"[{b1:.2f}, {b2:.2f}, {b3:.2f}]")
    max_value = max(b1, b2, b3)
    if max_value < 1:
        if to_print:
            print(f"{max_value} < 1 \nLogo, converge")
            print("="*35)
        return True
    else:
        if to_print:
            print(f"{max_value} >= 1 \nLogo, não converge")
            print("=="*35)
        return False


def is_caculable(coefs_a, to_print):
    if not checaCriterioLinha(coefs_a, to_print) and not checaCriterioSassenfeld(coefs_a, to_print):
        return False
    else:
        return True


def calculaGaussSeidel(coefs_a, coefs_b, x1=0, x2=0, x3=0, tol=10**(-2), n_iteracoes=10, graphic_on=True):
    divideCoeficiente(coefs_a, coefs_b)
    # if not is_caculable(coefs_a, to_print=True):
    #     return

    print("Método de Gauss-Seidel\n")

    # listas para armazenar resultados e erros
    resultados = [x1, x2, x3]
    n_variaveis = len(resultados)
    erros = []

    # listas para gráficos
    y_x1 = [x1]
    y_x2 = [x2]
    y_x3 = [x3]
    x_axis = [0]

    i = 0
    #while i < n_iteracoes:
    while True:
        x1 = -coefs_a[0][1] * x2 - coefs_a[0][2] * x3 + coefs_b[0][0]
        x2 = -coefs_a[1][0] * x1 - coefs_a[1][2] * x3 + coefs_b[1][0]
        x3 = -coefs_a[2][0] * x1 - coefs_a[2][1] * x2 + coefs_b[2][0]

        resultados.insert(0, x1)
        resultados.insert(1, x2)
        resultados.insert(2, x3)

        y_x1.append(x1)
        y_x2.append(x2)
        y_x3.append(x3)

        # este loop calcula os erros e exclui os itens que não são mais utéis das listas
        for j in range(0, n_variaveis):
            erros.append(resultados[j] - resultados[j + n_variaveis])

            if len(erros) > n_variaveis:
                del erros[j]

        i += 1
        x_axis.append(i)

        print(f"Número de iterações: {i}, x1 = {x1:.4f}, x2 = {x2:.4f}, x3 = {x3:.4f}")
        if (max(erros) / max(resultados)) < tol:
            break

    if graphic_on:
        plt.title('Solução do sistema - Método de Gauss-Seidel')
        plt.xlabel("Iterações")
        plt.ylabel("Valor de x calculado")
        plt.xticks(range(len(x_axis)))
        plt.plot(x_axis, y_x1, label="x1")
        plt.plot(x_axis, y_x2, label="x2")
        plt.plot(x_axis, y_x3, label="x3")
        plt.legend()
        plt.grid()
        plt.show()

    return x1, x2, x3


def calculaJacobi(coefs_a, coefs_b,  x1=0, x2=0, x3=0, tol=10**(-2), n_iteracoes=10, graphic_on=True):
    print("Método de Jacobi\n")
    divideCoeficiente(coefs_a, coefs_b)
    # listas para armazenar resultados e erros
    resultados = [x1, x2, x3]
    n_variaveis = len(resultados)
    erros = []

    # listas para gráficos
    y_x1 = [x1]
    y_x2 = [x2]
    y_x3 = [x3]
    x_axis = [0]

    i = 0
    #while i < n_iteracoes:
    while True:
        x1 = -coefs_a[0][1] * resultados[1] - coefs_a[0][2] * resultados[2] + coefs_b[0][0]
        x2 = -coefs_a[1][0] * resultados[0] - coefs_a[1][2] * resultados[2] + coefs_b[1][0]
        x3 = -coefs_a[2][0] * resultados[0] - coefs_a[2][1] * resultados[1] + coefs_b[2][0]

        resultados.insert(0, x1)
        resultados.insert(1, x2)
        resultados.insert(2, x3)

        y_x1.append(x1)
        y_x2.append(x2)
        y_x3.append(x3)

        # este loop calcula os erros e exclui os itens que não são mais utéis das listas
        for j in range(0, n_variaveis):
            erros.append(resultados[j] - resultados[j+n_variaveis])

            if len(erros) > n_variaveis:
                del erros[j]

        i += 1
        x_axis.append(i)

        print(f"Número de iterações: {i}, x1 = {x1:.4f}, x2 = {x2:.4f}, x3 = {x3:.4f}")
        if (max(erros) / max(resultados)) < tol:
            break

    if graphic_on:
        plt.title('Solução do sistema - Método de Jacobi')
        plt.xlabel("Iterações")
        plt.ylabel("Valor de x calculado")
        plt.xticks(range(len(x_axis)))
        plt.plot(x_axis, y_x1, label="x1")
        plt.plot(x_axis, y_x2, label="x2")
        plt.plot(x_axis, y_x3, label="x3")
        plt.legend()
        plt.grid()
        plt.show()

    return x1, x2, x3


def f(x):
    return -32 + 11*(x + 1) - 2*(x + 1)*(x - 2)


def derivada_fx(x, h=0.00001):
    return (f(x+h)-f(x))/h


def newton_raphson(x, tolerancia=10**(-12)):
    print("==" * 35)
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

