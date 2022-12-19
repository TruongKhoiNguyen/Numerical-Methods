import math
from tabulate import tabulate


def func(x):
    '''
    Real solution of f
    '''
    return 1 + 1/2 * math.exp(-4 * x) - 1/2 * math.exp(-2 * x)


def f(x, y):
    '''
    y' + 2y = 2 - exp(-4x)
    '''
    return 2 - math.exp(-4 * x) - 2 * y


def main():
    x = 0
    y = 1
    H = 0.1
    target = 10

    n = int(target / H)

    tracer = [[0, x, y]]

    for i in range(n):
        y = y + f(x, y) * H
        x = x + H
        exact = func(x)
        error = abs(exact - y)
        relative_error = error / exact
        tracer.append([i + 1, x, y, exact, error, relative_error])

    print(tabulate(tracer, headers=[
          'i', 'x', 'y', 'exact', 'error', 'relative error']))


if __name__ == '__main__':
    main()
