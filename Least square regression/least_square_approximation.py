import numpy as np
from tabulate import tabulate


def coefficient_matrix(x, degree):
    mat_material = [np.sum(list(map(lambda k: k ** i, x)))
                    for i in range(1, degree + 2)]

    n = len(x)
    mat_material.insert(0, n)

    mat_size = degree + 1
    mat = np.array([mat_material[i:i + mat_size] for i in range(mat_size)])

    return mat


def coefficient_vector(x, y, degree):
    n = len(y)

    return np.array([np.sum([x[j] ** i * y[j] for j in range(n)])
                     for i in range(degree + 1)])


def print_result(result):
    formatted_result = [[f'a{i}', result[i]]
                        for i in range(len(result))]
    print(tabulate(formatted_result))


def least_square_approximation(x, y, degree):
    mat = coefficient_matrix(x, degree)
    vec = coefficient_vector(x, y, degree)
    coefficients = np.linalg.solve(mat, vec)
    print_result(coefficients)


def main():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([1.3, 3.5, 4.2, 5.0, 7.0, 8.8, 10.1, 12.5, 13.0, 15.6])

    least_square_approximation(x, y, 1)


if __name__ == '__main__':
    main()
