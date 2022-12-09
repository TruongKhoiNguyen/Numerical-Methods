def formula(x):
    return 2 * (x ** 2)


def three_midpoint_differentiate(f, x0, h):
    return (f(x0+h)-f(x0-h))/(2*h)


# driver code
print(three_midpoint_differentiate(formula, 3, 0.5))
