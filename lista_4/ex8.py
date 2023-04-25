import matplotlib.pyplot as plt
from math import e
from numpy import log

initial_value = 0
stop_value = 10

y = [1]
t_values = [0]
y_exato = []


def t_list(initial_value, stop_value, h):
    t = 0

    while True:
        t += initial_value + h
        t_values.append(t)
        if round(t, 3) == stop_value:
            break
    return t_values


def calc_y():
    for i in range(0, len(t_values)):
        y_exato.append(log(-5*t_values[i]**2*e**(-t_values[i]) - 10*t_values[i]*e**(-t_values[i]) - 9*e**(-t_values[i]) + e + 9))
    return y_exato


def f(t, yi):
    fi = ((5*t**2)-yi)/(e**(t+yi))
    return fi


def rk4(h):
    for i in range(initial_value, len(t_values)-1):
        k1 = f(t_values[i], y[i])
        k2 = f(t_values[i]+h/2, y[i]+h/2*k1)
        k3 = f(t_values[i]+h/2, y[i]+h/2*k2)
        k4 = f(t_values[i]+h, y[i]+h*k3)
        k = (1 / 6) * (1*k1 + (0 * k2) + (5 * k3) + 0*k4)

        yn = y[i] + (h * k)
        y.append(yn)
    plt.plot(t_values, y, label=f"rk4, h = {h}")


def euler(h):
    for i in range(initial_value, len(t_values)-1):
        yn = y[i] + (h * f(t_values[i], y[i]))
        y.append(yn)
    plt.plot(t_values, y, label=f"euller, h = {h}")


#############################################

t_list(initial_value, stop_value, 0.1)
rk4(0.1)
y.clear()
y = [1]

euler(0.1)

############################################

plt.plot(t_values, calc_y(), label="solução PVI")
plt.grid()
plt.legend()
plt.show()
