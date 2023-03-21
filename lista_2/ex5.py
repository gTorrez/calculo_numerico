import numpy as np

import matplotlib.pyplot as plt

# Método de Jacobi-Richardson

# A: matriz que representa o sistema de equações
# D: é a matriz diagonal de A
# -L: é a matriz triangular inferior A
# -R: matriz triangular superior de A


def Jacobi (A,b,x0,tol,n):
    D = np.diag(np.diag(A))
    LR = A-D                                                 # matriz com diagonal zerada
    x = x0
    n_iteracoes = 0
    valores_iteracao = []                                    # lista vazia para armazenar os valores de cada iteração

    for i in range(n):
        D_inv = np.linalg.inv(D)                             # matriz inversa de D
        x_antigo = x
        x = np.dot(D_inv, np.dot(-LR,x))+np.dot(D_inv,b)

        print('iteração',i,': x =',x)
        valores_iteracao.append(x)                           # adiciona o valor de x à lista de valores da iteração

        # Verificando se o erro relativo é menor que a tolerância
        if (np.linalg.norm(x-x_antigo)/np.linalg.norm(x)) < tol:
            return x, i+1, valores_iteracao

    return x, i+1, valores_iteracao

#-------------------------------------------------------------------------------
# Questão 5

A = np.array([[10,2,1],[1,5,1],[2,3,10]])
b = np.array([7,-8,6])                      # matriz dos termos independentes
x0 = np.array([0.7,-1.6, 0.6])              # vetor de iniciação
E_tol = 10**-2                              # tolerância
n = 1000                                    # número máximo de iterações

x, n_iteracoes, valores_iteracao = Jacobi(A,b,x0,E_tol,n)

print('')
print('Resultado:')
print('Número de Iterações:',n_iteracoes)
print('Solução aproximada do sistema de equações: x =',x)
print('')

# Arredondando os resultados
print('Soluções arredondadas:')
print('x1 =',round(x[0]))
print('x2 =',round(x[1]))
print('x3 =',round(x[2]))

# Plotando o gráfico dos valores encontrados ao longo das iterações
plt.figure()
plt.title("Solução do sistema - Método de Jacobi")
plt.xlabel("Iteração")
plt.ylabel("Valor de x")

for i in range(len(x0)):
    valores_i = [v[i] for v in valores_iteracao]
    plt.plot(range(len(valores_i)), valores_i, label=f"x{i+1}")

plt.legend()
plt.grid()
plt.show()