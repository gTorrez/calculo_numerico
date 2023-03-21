import numpy as np

# Definir a matriz dos coeficientes
A = np.array([[4, -1, 1], [2, 5, 2], [1, 2, 4]])

# Definir o vetor dos termos independentes
B = np.array([8, 3, 11])

# Calcular o determinante da matriz dos coeficientes
det_A = np.linalg.det(A)

# Inicializar a lista de soluções
x = []

# Calcular as soluções do sistema de equações
for i in range(A.shape[0]):
    # Substituir a coluna i da matriz dos coeficientes pelos termos independentes
    A_i = A.copy()
    A_i[:, i] = B

    # Calcular o determinante da nova matriz
    det_A_i = np.linalg.det(A_i)

    # Calcular a solução correspondente
    x_i = det_A_i / det_A

    # Adicionar a solução à lista de soluções
    x.append(x_i)

# Imprimir as soluções
print("As soluções do sistema de equações são: ")
print("x1 =", x[0])
print("x2 =", x[1])
print("x3 =", x[2])

# Arredondando os valores
x1_rounded = round(x[0])
x2_rounded = round(x[1])
x3_rounded = round(x[2])

print("As soluções do sistema de equações arredondadas são: ")
print("x1 =", x1_rounded)
print("x2 =", x2_rounded)
print("x3 =", x3_rounded)