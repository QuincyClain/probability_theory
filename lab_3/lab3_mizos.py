from numpy.random import rand
import numpy as np
from matplotlib import pyplot as plt
from math import floor, pow
from matplotlib.widgets import Button

max_n = 50
a = -2
b = 4
COUNT_INTERVAL = 15
alpha = 0.01


def func(value):
    is_negative = value < 0
    result = pow(abs(value), 1 / 3)
    return -result if is_negative else result


borderA = func(a)
borderB = func(b)


def analytical_func_densiny(y):
    if y >= borderA and y <= borderB:
        return (1 / 2) * pow(y, 2)
    return 0


def analytical_func_dist(y):
    if y >= borderA and y <= borderB:
        return (1 / 6) * (pow(y, 3) - a)

    return 0 if y < borderA else 1


def add_analytical_func_densiny_to_plot():
    x_axis = np.linspace(func(a), func(b), 100)
    y_axis = [analytical_func_densiny(i) for i in x_axis]
    plt.step(x_axis, y_axis, label="analytical function densiny")
    plt.legend()


def add_analytical_func_dist_to_plot():
    x_axis = np.linspace(func(a), func(b), 1000)
    y_axis = [analytical_func_dist(i) for i in x_axis]
    plt.step(x_axis, y_axis, label="analytical function distribution")
    plt.legend()


def get_eps():
    return rand()


def get_x_sample(a, b, n):
    result = []
    for i in range(n):
        x = get_eps() * (b - a) + a
        result.append(x)
    return result


def get_y_sample(x_sample):
    result = []
    for x in x_sample:
        result.append(func(x))
    return sorted(result)


x_sample = get_x_sample(a, b, max_n)


# Вариационный ряд y_sample
y_sample = get_y_sample(x_sample)


def get_empiric_function_dist_values(y_sample):
    all = len(y_sample)
    y_axis = [0] + [cur / all for cur in range(all)] + [1]
    x_axis = [func(a)] + [y for y in y_sample] + [func(b)]
    return x_axis, y_axis


def add_empiric_function_to_plot(y_sample):
    x_axis, y_axis = get_empiric_function_dist_values(y_sample)
    plt.step(x_axis, y_axis, label="empiric")
    plt.legend()

def get_mizos(y_sample):
    result = 1 / (12 * len(y_sample))
    for i in range(len(y_sample)):
        result += pow(analytical_func_dist(y_sample[i]) - (i + 0.5) / len(y_sample), 2)
    return result


while True:
    x_sample = get_x_sample(a, b, max_n)
    y_sample = get_y_sample(x_sample)
    misoz = get_mizos(y_sample)
    print('Эмпирическое значение критерия мизоса: %f' % misoz)
    print('Табличное значение критерия мизоса: %f' % 0.744)
    add_analytical_func_dist_to_plot()
    add_empiric_function_to_plot(y_sample)
    plt.show()


