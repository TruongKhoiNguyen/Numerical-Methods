import math
import functools
import numpy as np


def forward_difference(x, y, xp):
    n = len(x)
    h = x[1] - x[0]
    r = (xp - x[0])/h

    difference_table = [y.tolist()]

    for i in range(1, n):
        difference_table.append(
            [difference_table[i - 1][j+1] - difference_table[i - 1][j] for j in range(n - i)])

    yp = 0
    product = 1
    for i in range(n):
        product *= functools.reduce(lambda a, b: a * b,
                                    [r - j for j in range(i)], 1)
        yp += difference_table[i][0] * product / math.factorial(i)

    print('Interpolated value:', yp)


def main():
    x = np.array([1.7, 1.8, 1.9, 2.0])
    y = np.array([0.3979849, 0.3399864, 0.2818186, 0.2238908])

    forward_difference(x, y, 1.72)


if __name__ == '__main__':
    main()
