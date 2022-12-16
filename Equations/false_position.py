import math
from tabulate import tabulate


N0 = 1000
TOL = 10**-4


def f(x):
    return math.cos(x) - x


def false_position(p0, p1):
    steps = []
    success = False
    p = 0

    q0 = f(p0)
    q1 = f(p1)
    for i in range(1, N0):
        p = p1 - q1 * (p1 - p0) / (q1 - q0)

        steps.append([i, p0, p1, p, f(p)])

        if abs(p - p1) < TOL:
            success = True
            break

        q = f(p)

        if q * q1 < 0:
            p0 = p1
            q0 = q1

        p1 = p
        q1 = q

    print(tabulate(steps, headers=['n', 'p0', 'p1', 'p', 'f(p)']), '\n')

    if (success):
        print(f'Solution: {p}')
    else:
        print('The procedure was unsuccessful')


def main():
    false_position(0.5, math.pi / 4)


if __name__ == '__main__':
    main()
