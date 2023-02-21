from math import sin


def biseccao(a, b, tolerancia=0.00000001):
    m_list = []
    i = 0

    print("Método da bissecção\n")
    while True:
        fa = (a/2)**2 - sin(a)

        m = (a+b)/2
        fm = (m/2)**2 - sin(m)

        if fa*fm < 0:
            a = a
            b = m

        else:
            a = m
            b = b

        i += 1

        m_list.append(m)
        if len(m_list) > 2:
            m_list.pop(0)

        if (len(m_list) == 2) and abs(m_list[1] - m_list[0]) <= tolerancia:
            break

    print(f"Número de iterações: {i}, Valor encontrado = {m:.10f}")


biseccao(1.5, 2)
