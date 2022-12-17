import numpy as np
from tabulate import tabulate


class JacobiSolver:
    def __init__(self, a, b, x0, n):
        self.A = a
        self.B = b
        self.N = n
        self.X0 = x0

        self.steps = []

    def solve(self):
        size = len(self.A)

        x = self.X0

        self.steps.append([0, *x.copy()])

        x_tmp = x.copy()
        for iter in range(1, self.N):
            for i in range(size):
                tmp = np.array([self.A[i][j] * x[j] for j in range(size)])
                sum = np.sum(tmp[:i]) + np.sum(tmp[i+1:])

                x_tmp[i] = (self.B[i] - sum) / self.A[i][i]

            x = x_tmp.copy()
            self.steps.append([iter, *x.copy()])

        headers = list(map(lambda x: f'x{x}', range(1, size + 1)))
        print(tabulate(self.steps, headers=headers))


class JacobiSolverBuilder:
    A = None
    B = None
    N = 25
    X0 = None

    def set_A(self, a):
        self.A = a

        return self

    def set_B(self, b):
        self.B = b

        return self

    def set_X0(self, x0):
        self.X0 = x0

        return self

    def set_N(self, n):
        self.N = n
        return self

    def build(self):
        return JacobiSolver(self.A, self.B, self.X0, self.N)


def main():
    A = np.array([[10, -1, 2, 0],
                  [-1, 11, -1, 3],
                  [2, -1, 10, -1],
                  [0, 3, -1, 8]])

    B = np.array([6, 25, -11, 15])

    JacobiSolverBuilder() \
        .set_A(A) \
        .set_B(B) \
        .set_X0(np.zeros(len(A))) \
        .set_N(15) \
        .build()  \
        .solve()


if __name__ == '__main__':
    main()
