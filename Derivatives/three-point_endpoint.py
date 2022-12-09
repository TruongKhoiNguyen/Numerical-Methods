import math

formula = input('Input the formula here : ')
n = int(input('Input the degree of derivative here: '))


def f(formula, x):
    return eval(formula, globals(), {'x': x})  # use global and local scope


# no error handling here - TODO
x0 = float(input('Input the approximation of x here : '))
h = float(input('Input the stepsize h here : '))


def TPEP(x, h, n, formula):  # Three Point End Point
    if n <= 1:  # need to check for iteration stop: the grade of derivatives
        return (1/(2*h))*(-3*f(formula, x)+4*f(formula, x+h)-f(formula, x+2*h))
    # error-term omitted
    return (1/(2*h))*(-3*TPEP(x, h, n-1, formula)+4*TPEP(x+h, h, n-1, formula)-TPEP(x+2*h, h, n-1, formula))


print('Derivative of f in x0 = {0} is : '.format(x0))
print("f'({0}) = {1:.7f} (Three Point Endpoint)".format(
    x0, TPEP(x0, h, n, formula)))
