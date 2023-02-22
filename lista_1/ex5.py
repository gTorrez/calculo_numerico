from math import pi

n = int(input("Insira o valor de n: "))
npi = 0

for i in range(0, n):
  npi = npi + ((16**(-i))*((4/((8*i)+1))-(2/((8*i)+4))-(1/((8*i)+5))-(1/((8*i)+6))))
  print(npi)

print(pi, "é valor de pi segundo a biblioteca math.")