from numpy.random import rand
import numpy as np
from matplotlib import pyplot as plt
from math import floor, pow
from matplotlib.widgets import Button

max_n = 100
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
    x_axis = np.linspace(func(a), func(b), 1000)
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


def equal_chance_method(y_sample):
    count = len(y_sample)
    take_points = count / COUNT_INTERVAL
    interval_count = count / COUNT_INTERVAL
    representative_eps = 6
    current = 0
    result = []

    while True:
        left = current
        right = round(take_points)

        if right >= len(y_sample):
            right = len(y_sample) - 1

        if abs(right - left + 1 - interval_count) <= representative_eps:
            result.append(
                (y_sample[left], y_sample[right], (right - left + 1) / (count * (y_sample[right] - y_sample[left]))))

        if right == count - 1:
            break

        current = right + 1

        take_points += interval_count

    return result


def add_equal_chance_method_to_plot(values):
    y_axis = []
    x_axis = []
    for i in values:
        y_axis.append(i[0])
        y_axis.append(i[1])
        x_axis.append(i[2])
        x_axis.append(i[2])
    plt.step(y_axis, x_axis, label="equal chance gistogram")
    plt.legend()


def get_hi_deviation(values):
    hi_deviation = 0
    s = 0
    empiric_prob = (1 / COUNT_INTERVAL)

    for i in values:
        diff = analytical_func_dist(i[1]) - analytical_func_dist(i[0])
        hi_deviation += (pow(diff - empiric_prob, 2)) / diff
        s += diff

    hi_deviation *= max_n
    return hi_deviation


while True:
    x_sample = get_x_sample(a, b, max_n)
    y_sample = get_y_sample(x_sample)
    values = equal_chance_method(y_sample)
    k = COUNT_INTERVAL - 1
    hi = get_hi_deviation(values)
    permissible = 29.1
    betta = 0.05

    print('Число степеней свободы: %i' % k)
    print('Уровень значимости: %f' % alpha)
    print('Критерий пирсона хи квадрат: %f' % hi)
    print('Допустимое табличное значение: %f' % permissible)

    add_equal_chance_method_to_plot(values)
    add_analytical_func_densiny_to_plot()
    plt.show()