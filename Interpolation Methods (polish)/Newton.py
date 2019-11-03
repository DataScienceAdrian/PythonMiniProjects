def interpolacja_Newtona(x, y, x1):
    g = y[:]
    s = g[0]

    for i in range(len(y) - 1):
        g = [(g[j + i] - g[j]) / (x[j + i + 1] - x[j]) for j in range(len(g) - 1)]
        s += g[0] * iterator(x1 - x[j] for j in range(i + 1))
    return s


def iterator(a):
    q = 1
    for i in a: q *= i
    return q


if __name__ == '__main__':
    y = [1, 3, 2, 5, 7]
    x = [0, 2, 3, 4, 6]
    x1 = 1
    wynik = interpolacja_Newtona(x, y, x1)
    print(wynik)
