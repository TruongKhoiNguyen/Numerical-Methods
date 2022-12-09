Matrix = list[list]


def lu_decomposition(mat: Matrix) -> list[Matrix]:
    '''
    This function assumes that the matrix has the size n x n.
    This function use Doolittle method to decompose the input matrix
    '''

    n: int = len(mat)

    upper: Matrix = [[0 for x in range(n)] for y in range(n)]
    lower: Matrix = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(0, i):
                sum += lower[i][k] * upper[k][j]

            upper[i][j] = mat[i][j] - sum

        for j in range(i, n):
            if i == 0:
                lower[j][i] = mat[j][i] / upper[i][i]

            else:
                sum = 0
                for k in range(0, i):
                    sum += lower[j][k] * upper[k][i]

                lower[j][i] = (mat[j][i] - sum) / upper[i][i]

    result = [lower, upper]

    return result


def forward_substitution(mat: Matrix, vec: list) -> list[float]:
    n: int = len(mat)

    result: list[float] = []

    for i in range(n):
        sum = 0
        for j in range(i):
            sum += mat[i][j] * result[j]

        result.append((vec[i] - sum) / mat[i][i])

    return result


def backward_substitution(mat: Matrix, vec: list) -> list[float]:
    n: int = len(mat)

    result: list[float] = [0 for i in range(n)]

    for i in reversed(range(n)):
        sum = 0
        for j in range(i, n):
            sum += mat[i][j] * result[j]

        result[i] = (vec[i] - sum) / mat[i][i]

    return result


def lu_solver(mat: Matrix, vec: list[float]) -> list[float]:
    factorization: list[Matrix] = lu_decomposition(mat)

    L: Matrix = factorization[0]
    U: Matrix = factorization[1]

    y: list[float] = forward_substitution(L, vec)
    x: list[float] = backward_substitution(U, y)

    return x


def main() -> None:
    mat: Matrix = [[2, 1, -2],
                   [3, -3, -1],
                   [1, -2, 3]]

    vec: list[float] = [-1, 5, 6]

    result: list = lu_solver(mat, vec)

    print(result)


if __name__ == '__main__':
    main()
