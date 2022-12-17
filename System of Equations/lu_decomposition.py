import numpy as np
from tabulate import tabulate

Matrix = list[list]


def doolittle(mat):
    n = len(mat)

    for i in range(n):
        # calculate part for L
        for j in range(0, i):
            a = mat[i][j]
            for p in range(0, j):
                a = a - mat[i][p] * mat[p][j]

            mat[i][j] = a / mat[j][j]

        # calculate part for U
        for j in range(i, n):
            a = mat[i][j]
            for p in range(0, i):
                a = a - mat[i][p] * mat[p][j]

            mat[i][j] = a

    U = np.triu(mat)

    L = np.tril(mat, k=-1)
    np.fill_diagonal(L, 1)

    return L, U


def forward_substitution(mat, vec: list) -> list[float]:
    """
    Solve Ly = b
    """
    n: int = len(mat)

    result: list[float] = []

    for i in range(n):
        sum = 0
        for j in range(i):
            sum += mat[i][j] * result[j]

        result.append((vec[i] - sum) / mat[i][i])

    return result


def backward_substitution(mat, vec: list) -> list[float]:
    """
    Solve: Ux = y
    """
    n: int = len(mat)

    result: list[float] = [0 for i in range(n)]

    for i in reversed(range(n)):
        sum = 0
        for j in range(i, n):
            sum += mat[i][j] * result[j]

        result[i] = (vec[i] - sum) / mat[i][i]

    return result


def lu_solver(mat, vec: list[float]) -> list[float]:
    L, U = doolittle(mat)

    print('L: ')
    print(tabulate(L, tablefmt='simple_grid'))
    print('U: ')
    print(tabulate(U, tablefmt='simple_grid'), '\n')

    y: list[float] = forward_substitution(L, vec)
    x: list[float] = backward_substitution(U, y)

    return x


def main() -> None:
    mat = np.array([[7, -2, 1],
                    [14, -7, -3],
                    [-7, 11, 18]])

    vec: list[float] = [12, 17, 5]

    # Solutions: [3, 4, -1]

    result: list = lu_solver(mat, vec)

    print('Solution:', result)


if __name__ == '__main__':
    main()
