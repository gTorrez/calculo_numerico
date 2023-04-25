import matplotlib.pyplot as plt
from math import e

initial_value = 0
stop_value = 2.5

y = [1]
t_values = [0]

def t_list(initial_value, stop_value, h):
    t = 0

    while True:
        t += initial_value + h
        t_values.append(t)
        if round(t, 3) == stop_value:
            break
    return t_values


def calc_y():
    y_exato = []
    for i in range(0, len(t_values)):
        y_exato.append(e ** (-t_values[i]) + t_values[i])
    return y_exato


def f(t, yi):
    fi = -yi + t + 1
    return fi


def euler(h):
    for i in range(initial_value, len(t_values)-1):
        yn = y[i] + (h * f(t_values[i], y[i]))
        y.append(yn)

    plt.plot(t_values, y, label=f"h = {h}")

    print(f"h = {h}, y(5) = {y[len(y)-1]:.3f}")
    return y


#############################################
t_list(initial_value, stop_value, 0.5)
euler(0.5)

t_values.clear()
y.clear()
y = [1]
t_values = [0]

t_list(initial_value, stop_value, 0.1)
euler(0.1)

t_values.clear()
y.clear()
y = [1]
t_values = [0]

t_list(initial_value, stop_value, 0.05)
euler(0.05)

y.clear()
y = [1]

y_real = calc_y()
print(f"Solução real: y(5) = {y_real[len(y_real)-1]:.3f}")
##########################################################

plt.plot(t_values, calc_y(), label="e^(-t) + t")
plt.grid()
plt.legend()
plt.show()
