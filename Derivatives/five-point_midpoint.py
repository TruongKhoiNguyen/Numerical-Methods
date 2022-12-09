def formula(x):
    return 2 * (x ** 2)


def five_midpoint_differentiate(f, x0, h):
    return (f(x0-2*h) - 8*f(x0-h)+8*f(x0+h)-f(x0+2*h))/(12*h)


# driver code
print(five_midpoint_differentiate(formula, 3, 0.5))
