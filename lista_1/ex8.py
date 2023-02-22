r = 0.401
s = 42.7*(10**(-6))
n_molec = 1000
t = 300
p = 3.5*(10**7)
k = 1.3806503 * (10**(-23))

tol = 10**(-12)

def biseccao(a, b, tolerancia=0.00000001):
    i = 0

    print("Método da bissecção")
    while abs(b-a)/2 > tolerancia:
        fa = (p + r * (n_molec/a)**2)*(a-n_molec*s)*(1/(k*n_molec*t))
        fb = (p + r * (n_molec/b)**2)*(b-n_molec*s)*(1/(k*n_molec*t))
        if fa*fb >= 0 and i == 0:
            print("Intervalo inválido pois não satisfaz f(a)f(b) < 0")
            return

        m = (a+b)/2
        fm = (p + r * (n_molec/m)**2)*(m-n_molec*s)*(1/(k*n_molec*t))

        if fa*fm < 0:
            b = m
        else:
            a = m

        i += 1

    print(f"Número de iterações: {i}, Valor encontrado = {m:.10f}")
    return m


def derivada(x, h=0.00001):
    # mudar função fx e fxh para calcular a derivada
    fx = (p + r * (n_molec / x) ** 2) * (x - n_molec * s) * (1 / (k * n_molec * t))
    fxh = (p + r * (n_molec / (x+h)) ** 2) * ((x+h) - n_molec * s) * (1 / (k * n_molec * t))
    resultado = (fxh-fx)/h
    return resultado


def newton_raphson(x, tolerancia):
    print("Método newton-raphson")
    i = 0
    xk_next = 0

    while abs(xk_next-x) > tolerancia:
        if i != 0:
            x = xk_next

        # mudar esta função
        valor_f = (p + r * (n_molec / x) ** 2) * (x - n_molec * s) * (1 / (k * n_molec * t))
        valor_derivada_f = derivada(x)
        xk_next = x - valor_f/valor_derivada_f

        i += 1

    print(f"Número de iterações: {i}, Valor encontrado = {xk_next:.10f}")
    return xk_next


def falsa_posicao(a, b, tolerancia=0.00000000001):
    print("Método falsa posição")
    xk_list = []
    i = 0

    while True:
        # mudar funções
        fa = (p + r * (n_molec / a) ** 2) * (a - n_molec * s) * (1 / (k * n_molec * t))
        fb = (p + r * (n_molec / b) ** 2) * (b - n_molec * s) * (1 / (k * n_molec * t))

        xk = ((a*fb)-(b*fa))/(fb-fa)
        # mudar função
        fxk = (p + r * (n_molec / xk) ** 2) * (xk - n_molec * s) * (1 / (k * n_molec * t))

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


biseccao(-1.0, 1000.0, tol)
print("=="*30)
falsa_posicao(0.01, 20, tol)
print("=="*30)
newton_raphson(0.01, tol)
print("=="*30)
