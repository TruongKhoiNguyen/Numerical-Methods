def formula(x):
    return 2 * (x ** 3)


def second_midpoint_derivatives(f, x0, h):
    return (f(x0 - h) - 2 * f(x0) + f(x0 + h)) / (h ** 2)


# driver code
print(second_midpoint_derivatives(formula, 2, 0.5))
