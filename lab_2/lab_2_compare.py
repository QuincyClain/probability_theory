from random import random
import numpy as np
from matplotlib import pyplot as plt
from lab_2_interval import equal_range_method, add_equal_range_method_to_plot
from lab2_chanсe import add_equal_chance_method_to_plot, equal_chance_method


max_n = 1000
a = -2
b = 4
COUNT_INTERVAL = 20


def func(value):
    is_negative = value < 0
    result = pow(abs(value), 1 / 3)
    return -result if is_negative else result


def analytical_func_densiny(y):
    if y >= borderA and y <= borderB:
        return (1 / 2) * (y ** 2)
    return 0


def add_analytical_func_to_plot():
    x_axis = np.linspace(func(a), func(b), 1000)
    y_axis = [analytical_func_densiny(i) for i in x_axis]
    plt.step(x_axis, y_axis, label="analytical function densiny")
    plt.legend()


borderA = func(a)
borderB = func(b)

def get_eps():
    return random()


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
y_sample = get_y_sample(x_sample)


add_analytical_func_to_plot()
equal_chance_values = equal_chance_method(y_sample)
add_equal_chance_method_to_plot(equal_chance_values)
equal_range_values = equal_range_method(y_sample)
add_equal_range_method_to_plot(equal_range_values)
plt.show()