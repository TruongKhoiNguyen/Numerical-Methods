from tabulate import tabulate

TOL = 10**-4
N0 = 1000


def bisection(f, a, b):
    calculation_step = []

    fa = f(a)

    for i in range(1, N0):
        p = a + (b - a) / 2
        fp = f(p)

        calculation_step.append([i, a, b, p, fp])

        if fp == 0 or (b - a) / 2 < TOL:
            break

        if fa * fp > 0:
            a = p
            fa = fp

        else:
            b = p

    print(tabulate(calculation_step, headers=['n', 'a', 'b', 'p', 'f(p)']))


def main():
    bisection(lambda x: x**3 + 4*x**2 - 10, 1.0, 2.0)


if __name__ == '__main__':
    main()
