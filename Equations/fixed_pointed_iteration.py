from tabulate import tabulate

N0 = 1000
TOL = 10**-4


def f(x):
    return 2*x**2 - 2*x - 5


def g(x):
    return ((2*x + 5) / 2)**(1/3)


def fixed_pointed_iteration(p0):
    """
    Condition: g'(x0) < 1
    """

    steps = []
    success = False
    p = 0
    for i in range(1, N0):
        p = g(p0)

        steps.append([i, p0, p, f(p)])

        if abs(p - p0) < TOL:
            success = True
            break

        p0 = p

    print(tabulate(steps, headers=['n', 'p0', 'p', 'f(p)']), '\n')

    if (success):
        print(f'Solution: {p}')
    else:
        print('The procedure was unsuccessful')


def main():
    fixed_pointed_iteration(1.5)


if __name__ == '__main__':
    main()
