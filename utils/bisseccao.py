r = 0.401
s = 42.7*(10**(-6))
n_molec = 1000
t = 300
p = 3.5*(10**7)
k = 1.3806503 * (10**(-23))

def biseccao(a, b, tolerancia=0.00000001):
    i = 0

    print("Método da bissecção\n")
    while abs(b-a)/2 > tolerancia:
        fa = (p + r * (n_molec/a)**2)*(a-n_molec*s)*(1/(k*n_molec*t))
        fb = (p + r * (n_molec/b)**2)*(b-n_molec*s)*(1/(k*n_molec*t))
        if fa*fb >= 0 and i == 0:
            print("Intervalo inválido pois não satisfaz f(a)f(b) < 0")
            return

        m = (a+b)/2
        fm = (p + r * (n_molec/m)**2)*(m-n_molec*s)*(1/(k*n_molec*t))
        if fm == 0:
            break

        if fa*fm < 0:
            a = a
            b = m

        else:
            a = m
            b = b
        i += 1

    print(f"Número de iterações: {i}, Valor encontrado = {m:.10f}")


biseccao(0.00001, 1)
