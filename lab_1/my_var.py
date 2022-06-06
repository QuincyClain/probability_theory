import numpy as np
from numpy.random import rand, normal

plot_dots = 10**3
b, a = -4, 2
def phi(x): return np.cbrt(x)


L, R = phi(b), phi(a)


def Y(): return phi(a+(b-a) * rand())


def func(value):
    is_negative = value < 0
    result = pow(abs(value), 1 / 3)
    return -result if is_negative else result


borderA = func(a)
borderB = func(b)


def f(y):
    if y >= borderA and y <= borderB:
        return (1 / 2) * (y ** 2)
    return 0

#проинтегрировал
def F(y):
    if y < np.cbrt(-4):
        return 0
    if y < np.cbrt(2):
        return 2/3 + (y**3)/6
    return 1


def M(): return 0.4787


def D(): return 1.09626
