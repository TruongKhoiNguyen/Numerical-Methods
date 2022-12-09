MAX_ITERATION = 100000

# Example function for calculation
# x^3 - x^2 + 2


def func(x: float) -> float:
    return x**3 - x**2 + 2


def false_position(a: float, b: float) -> None:
    if func(a) * func(b) >= 0:
        print('You have not assumed right a and b')
        return

    c = a

    for i in range(MAX_ITERATION):
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))

        if func(c) == 0:
            break

        elif func(c) * func(a) < 0:
            b = c

        else:
            a = c

    print(f'The value of root is: {c:.4f}')


def main():
    a = -200
    b = 300
    false_position(a, b)


if __name__ == '__main__':
    main()
