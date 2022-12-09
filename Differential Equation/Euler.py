from tabulate import tabulate


def f(x, y):
    return x + y


def main():
    x = 0
    y = 1
    H = 0.1
    target = 1

    n = int(target / H)

    tracer = [[0, x, y]]

    for i in range(n):
        y = y + f(x, y) * H
        x = x + H
        tracer.append([i + 1, x, y])

    print(tabulate(tracer, headers=['i', 'x', 'y']))


if __name__ == '__main__':
    main()
