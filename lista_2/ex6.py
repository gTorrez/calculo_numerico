import matplotlib.pyplot as plt

# definindo condiçõess iniciais e tolerância
x1 = 0
x2 = 0
x3 = 0
tol = 10**(-2)

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
while True:
    x1 = -0.20*x2 - 0.20*x3 + 1.00
    x2 = -0.75*x1 - 0.25*x3 + 1.50
    x3 = -0.50*x1 - 0.50*x2

    resultados.append(x1)
    resultados.append(x2)
    resultados.append(x3)

    y_x1.append(x1)
    y_x2.append(x2)
    y_x3.append(x3)

    # este loop calcula os erros e exclui os itens que não são mais utéis das listas
    for j in range(0, n_variaveis):
        if len(resultados) > 2*n_variaveis:
            del resultados[j]

        erros.append(resultados[j+n_variaveis] - resultados[j])

        if len(erros) > n_variaveis:
            del erros[j]

    i += 1
    x_axis.append(i)

    print(f"Número de iterações: {i}, x1 = {x1:.4f}, x2 = {x2:.4f}, x3 = {x3:.4f}")
    if (max(erros)/max(resultados)) < tol:
        break


plt.xticks(range(len(x_axis)))
plt.plot(x_axis, y_x1, label="x1")
plt.plot(x_axis, y_x2, label="x2")
plt.plot(x_axis, y_x3, label="x3")
plt.legend()
plt.grid()
plt.show()
