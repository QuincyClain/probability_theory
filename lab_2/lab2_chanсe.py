from random import random
import numpy as np
from matplotlib import pyplot as plt

max_n = 100
a = -2
b = 4
COUNT_INTEVAL = 10


def func(value):
    is_negative = value < 0
    result = pow(abs(value), 1 / 3)
    return -result if is_negative else result


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

def equal_chance_method(y_sample):
    count = len(y_sample)
    take_points = count / COUNT_INTEVAL
    interval_count = count / COUNT_INTEVAL
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


equal_chance_values = equal_chance_method(y_sample)
add_equal_chance_method_to_plot(equal_chance_values)
plt.show()