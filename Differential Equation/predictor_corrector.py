from tabulate import tabulate


def f(x, y):
    return x + y


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

        tracer.append([i + 1, x, y, f_half])

    print(tabulate(tracer, headers=['i', 'x', 'y', 'f_half']))


if __name__ == '__main__':
    main()
