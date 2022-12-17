import functools
import numpy as np


def newton(x, y, xp):
    n = len(x)
    difference_table = [y.tolist()]

    for i in range(1, n):
        difference_table.append([(difference_table[i - 1][j + 1] - difference_table[i - 1][j]) / (x[j + i] - x[j])
                                for j in range(len(difference_table[i - 1]) - 1)])

    yp = functools.reduce(lambda a, b: a + b, [difference_table[i][0] * functools.reduce(
        lambda a, b: a * b, map(lambda x: xp - x, x[:i]), 1) for i in range(n)])

    print('Interpolated value:', yp)


def main():
    x = np.array([8.0, 9.0, 9.5, 11.0])
    y = np.array([2.079442, 2.197225, 2.251292, 2.397895])

    newton(x, y, 9.2)


if __name__ == '__main__':
    main()
