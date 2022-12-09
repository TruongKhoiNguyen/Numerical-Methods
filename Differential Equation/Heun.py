from tabulate import tabulate


def f(x, y):
    return x + y


def predictor(x, y, h):
    return y + f(x, y) * h


def main():
    x = 0
    y = 1
    H = 0.1
    yp = predictor(x, y, H)
    target = 1

    n = int(target / H)

    tracer = [[0, x, y, yp]]

    for i in range(n):
        y = y + (f(x, y) + f(x + H, yp)) / 2 * H
        x = x + H
        yp = predictor(x, y, H)

        tracer.append([i + 1, x, y, yp])

    print(tabulate(tracer, headers=['i', 'x', 'y', 'predictor']))


if __name__ == '__main__':
    main()
