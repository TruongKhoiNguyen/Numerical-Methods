import functools
import numpy as np


def lagrange(x, y, xp):
    n = len(x)
    yp = 0

    for i in range(n):
        p = functools.reduce(lambda a, b: a * b, map(lambda e: (xp - e) /
                             (x[i] - e), np.concatenate([x[:i], x[i+1:]])))

        yp = yp + p * y[i]

    return yp


def main():
    x = np.array([9.0, 9.5, 11])
    y = np.array([2.1972, 2.2513, 2.3979])

    print('Interpolated value:', lagrange(x, y, 9.2))


if __name__ == '__main__':
    main()
