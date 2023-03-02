import sys


# Essas linhas atribuem às variáveis max, min e epsilon os valores máximos, mínimos e "epsilon" de máquina para números em ponto flutuante. Acessamos esses valores através do atributo float_info do módulo sys.
# Mostra o maior número flutuante
max = sys.float_info.max
# Mostra o menor número flutuante
min = sys.float_info.min
# Mostra o epsilon da máquina
epsilon = sys.float_info.epsilon


print("O maior número flutuante possível de se usar em um computador é o %s, enqunto o menor é %s. Já o epsilon é igual a %s." %(max, min, epsilon))


def expressao(x):
    resultado = ((1+x)-1)/x
    return resultado


x = int(input("Insira o valor de x: "))
print("O resultado da expressão é:", expressao(x))


v_esperado = 1

for x in [1e-15, 1e+15]:
  e = ((1+x)-1)/x
  erro_abs = e - v_esperado
  print('Valor obtido =', e)
  print('Erro Absoluto =', abs(erro_abs))
  print('Erro Relativo =', abs(erro_abs/v_esperado))
  print('-'*40)

