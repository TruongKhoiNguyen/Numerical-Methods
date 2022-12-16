import numpy as np
from tabulate import tabulate


def print_matrix(mat):
    print(tabulate(mat, tablefmt='simple_grid'))


def gaussian_elimination(a):
    print_matrix(a)

    n = len(a)

    success = True
    for k in range(n - 1):
        # swap row to avoid 0
        m = k

        for j in range(k + 1, n):
            if a[m][k] < a[j][k]:
                m = j

        if a[m][k] == 0:
            success = False
            break

        a[[k, m]] = a[[m, k]]

        if a[n - 1][n - 1] == 0:
            success = False
            break

        # eliminate rows below
        for j in range(k + 1, n):
            mjk = a[j][k] / a[k][k]

            for p in range(k + 1, n + 1):
                a[j][p] = a[j][p] - mjk * a[k][p]

        print_matrix(a)

    print('\n')

    if success:
        print('Solutions:')
        x = np.zeros(n)

        x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

        for i in reversed(range(0, n - 1)):
            sum = 0
            for j in range(i + 1, n):
                sum += a[i][j] * x[j]

            x[i] = 1 / a[i][i] * (a[i][n] - sum)

        for i in range(n):
            print(f'  x{i}: {x[i]}')

    else:
        print('No unique solution exist')


def main():
    mat = np.array([[0, 8, 2, -7],
                    [3, 5, 2, 8],
                    [6, 2, 8, 26]],
                   dtype=np.float64)

    gaussian_elimination(mat)


if __name__ == '__main__':
    main()
