from math import *


def interpolacja_lagrange(x, y, u):
    r = range(len(y))
    a = [y[i] / produkt(x[i] - x[j] for j in r if j != i) for i in r]
    return sum(a[i] * produkt([u - x[j] for j in r if j != i]) for i in r)


def produkt(a):
    b = 1
    for i in a: b *= i
    return b


if __name__ == '__main__':
    x = [-4, -2, 0, 2, 4]
    y = [876, 50, 0, 102, 1268]
    x1 = 1
    przewidywany = interpolacja_lagrange(x, y, x1)
    rzeczywisty = log(x1)
    print(przewidywany, rzeczywisty)
