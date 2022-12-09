from cmath import sqrt

Matrix = list[list[float]]


def cholesky_banachiewicz_decomposition(mat: Matrix) -> Matrix:
    n = len(mat)

    result: Matrix = [[0.0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(i + 1):
            sum = 0
            for k in range(j):
                sum += result[i][k] * result[j][k]

            if i == j:
                result[i][j] = sqrt(mat[i][i] - sum).real
            else:
                result[i][j] = (1.0 / result[j][j] * (mat[i][j] - sum))

    return result


def print_matrix(mat: Matrix) -> None:
    print('\n'.join([' '.join([f'{item:.4g}' for item in row])
                     for row in mat]))


def transpose(mat) -> Matrix:
    n = len(mat)

    result: Matrix = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            result[i][j] = mat[j][i]

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


def cholesky_solver(mat: Matrix, vec: list[float]) -> list[float]:
    L = cholesky_banachiewicz_decomposition(mat)
    L_transpose = transpose(L)

    y = forward_substitution(L, vec)
    x = backward_substitution(L_transpose, y)

    return x


def main() -> None:
    mat: Matrix = [[6, 15, 55],
                   [15, 55, 225],
                   [55, 225, 979]]

    vec: list[float] = [76, 295, 1259]

    result = cholesky_solver(mat, vec)

    print(result)


if __name__ == '__main__':
    main()
