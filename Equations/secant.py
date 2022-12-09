# function takes value of x
# and returns func(x)
def func(x: float) -> float:

    # we are taking equation
    # as x^3+x-1
    f = pow(x, 3) + x - 1
    return f


def secant(x1: float, x2: float, epsilon: float) -> None:
    n = 0
    xm = 0
    x0 = 0
    c = 0
    if (func(x1) * func(x2) < 0):
        while True:

            # calculate the intermediate value
            x0 = ((x1 * func(x2) - x2 * func(x1)) /
                  (func(x2) - func(x1)))

            # check if x0 is root of
            # equation or not
            c = func(x1) * func(x0)

            # update the value of interval
            x1 = x2
            x2 = x0

            # update number of iteration
            n += 1

            # if x0 is the root of equation
            # then break the loop
            if (c == 0):
                break
            xm = ((x1 * func(x2) - x2 * func(x1)) /
                  (func(x2) - func(x1)))

            if (abs(xm - x0) < epsilon):
                break

        print("Root of the given equation =",
              round(x0, 6))
        print("No. of iterations = ", n)

    else:
        print("Can not find a root in ",
              "the given interval")

# Driver code


# initializing the values
x1 = 0
x2 = 1
EPSILON = 0.0001
secant(x1, x2, EPSILON)
