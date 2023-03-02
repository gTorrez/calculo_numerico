tolerancia = 10**(-4) # tolerância enunciada
npi = 0
i = 0
pi = 3.141592 # valor de pi enunciado


while abs(pi - npi) > tolerancia: # checar se a aproximação de pi tem a precisão de 10e-4
  npi = npi + ((16**(-i))*((4/((8*i)+1))-(2/((8*i)+4))-(1/((8*i)+5))-(1/((8*i)+6)))) # expressão para calcular a série
  print(f'n = {i}; pi = {round(npi, 4)}')
  i += 1


print(f'Para valores de n >= {i-1} se obtém uma aproximação de pi com precisão de {tolerancia:.0e} ')
# a variável 'i' denota o numero de iterações e não o valor de n na expressão #
print(f'O valor de pi enunciado é {pi}')
print(f'O valor de pi calculado é {npi}')