import numpy as np


def compute_transformation_matrix(N):
    return np.fft.fft(np.eye(N))


def DFT(x):
    N = len(x)

    DFT_matrix = compute_transformation_matrix(N)
    result = DFT_matrix.dot(x)

    return result


def main():
    input_signal = np.array([4, 0, 3, 6, 2, 9, 6, 5])

    result = DFT(input_signal)

    print(result)


if __name__ == '__main__':
    main()
