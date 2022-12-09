# An example function whose solution
# is determined using Bisection Method.
# The function is x^3 - x^2 + 2
def func(x: float) -> float:
    return x * x * x - x * x + 2

# Derivative of the above function
# which is 3*x^x - 2*x


def derived_func(x: float) -> float:
    return 3 * x * x - 2 * x

# Function to find the root


def newton_calc(x: float) -> float:
    h = func(x) / derived_func(x)
    while abs(h) >= 0.0001:
        h = func(x)/derived_func(x)

        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h

    print("The value of the root is : ",
          "%.4f" % x)


# Driver program to test above
x0 = -20  # Initial values assumed
newton_calc(x0)
