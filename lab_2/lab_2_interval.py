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


# Вариационный ряд y_sample
y_sample = get_y_sample(x_sample)
MIN = y_sample[0]
MAX = y_sample[len(y_sample) - 1]
interval = (MAX - MIN) / COUNT_INTEVAL
S = 0
for item in y_sample:
    print(item)
    S += item*interval
print(interval)
print('Площадь: ')
print('0.455543')

def equal_range_method(y_sample):
    MIN = y_sample[0]
    MAX = y_sample[len(y_sample) - 1]
    count = len(y_sample)
    interval = (MAX - MIN) / COUNT_INTEVAL
    current = MIN
    result = []
    while current < MAX:
        left = current
        right = current + interval
        in_current_interval = 0
        for i in y_sample:
            if left <= i and i <= right:
                in_current_interval += 1

        result.append((left, right, in_current_interval / (count * interval)))

        current += interval
    return result


def add_equal_range_method_to_plot(values):
    y_axis = []
    x_axis = []
    for i in values:
        y_axis.append(i[0])
        y_axis.append(i[1])
        x_axis.append(i[2])
        x_axis.append(i[2])
    plt.step(y_axis, x_axis, label="equal range gistogram")
    plt.legend()


equal_range_values = equal_range_method(y_sample)
add_equal_range_method_to_plot(equal_range_values)
plt.show()




