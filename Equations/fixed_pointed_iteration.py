import math


# Function x^3 + x^2 - 1
def f(x: float) -> float:
    return x*x*x + x*x - 1


# Re-writing f(x)=0 to x = g(x)
def g(x: float) -> float:
    return 1/math.sqrt(1+x)


# Implementing Fixed Point Iteration Method
def fixed_point_iteration(x0: float, epsilon: float, N: int) -> None:
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    x1 = 0
    condition = True
    while condition:
        x1 = g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1

        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > epsilon

    if flag == 1:
        print(f'\nRequired root is: {x1:.8f}')
    else:
        print('\nNot Convergent.')


# Input Section
x0 = input('Enter Guess: ')
epsilon = input('Tolerable Error: ')
N = input('Maximum Step: ')

# Converting x0 and epsilon to float
x0 = float(x0)
epsilon = float(epsilon)

# Converting N to integer
N = int(N)

fixed_point_iteration(x0, epsilon, N)
