from tabulate import tabulate
import math


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


def predictor(x, y, h):
    return y + f(x, y) * h / 2


def main():
    x = 0
    y = 1
    H = 0.1
    yp = predictor(x, y, H)
    f_half = f(x + 1/2 * H, yp)
    target = 1

    n = int(target / H)

    tracer = [[0, x, y, f_half]]

    for i in range(n):
        y = y + f_half * H
        x = x + H
        yp = predictor(x, y, H)
        f_half = f(x + 1/2 * H, yp)

        exact = func(x)
        error = abs(exact - y)
        relative_error = error / exact

        tracer.append([i + 1, x, y, exact, error, relative_error])

    print(tabulate(tracer, headers=[
          'i', 'x', 'y', 'exact', 'error', 'relative error']))


if __name__ == '__main__':
    main()
