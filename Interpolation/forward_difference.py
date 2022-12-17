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

    print(difference_table)

    yp = 0
    product = 1
    for i in range(n):
        product *= functools.reduce(lambda a, b: a * b,
                                    [r - j for j in range(i)], 1)
        yp += difference_table[i][0] * product / math.factorial(i)

    print('Interpolated value:', yp)


def main():
    x = np.array([8.0, 9.0, 10.0, 11.0])
    y = np.array([2.07944154, 2.19722458, 2.30258509, 2.39789527])
    forward_difference(x, y, 9.2)


if __name__ == '__main__':
    main()
