def formula(x):
    return 2 * (x ** 2)


def five_endpoint_differentiate(f, x0, h):
    return (-25*f(x0)+48*f(x0+h)-36*f(x0+2*h)+16*f(x0+3*h)-3*f(x0+4*h))/(12*h)


# driver code
print(five_endpoint_differentiate(formula, 3, 0.5))
