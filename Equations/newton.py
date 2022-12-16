from tabulate import tabulate

N0 = 1000
TOL = 10**-4


def f(x) -> float:
    """
    Function to find solution
    """
    return x**2 - 2


def df(x) -> float:
    """
    Derivative of f
    """
    return 2*x


def newton(p0: float):
    """
    Condition: f need to be differentiable
    """
    steps = []
    success = False
    p = 0
    for i in range(1, N0):
        p = p0 - f(p0) / df(p0)

        steps.append([i, p0, p, f(p)])

        if abs(p - p0) < TOL:
            success = True
            break

        p0 = p

    print(tabulate(steps, headers=['n', 'p0', 'p', 'f(p)']))

    if (success):
        print(f'Solution: {p}')
    else:
        print('The procedure was unsuccessful')


def main():
    newton(2)


if __name__ == '__main__':
    main()
