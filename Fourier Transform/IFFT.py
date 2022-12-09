import numpy as np


def compute_transformation_matrix(N):
    DFT_matrix = np.fft.fft(np.eye(N))
    IFFT_matrix = (1 / N) * DFT_matrix.transpose()

    return IFFT_matrix


def IFFT(f):
    N = f.size

    IFFT_matrix = compute_transformation_matrix(N)
    result = IFFT_matrix.dot(f)

    return result


def main():
    frequencies = np.array([0, 0, 0, 0, 8, 0, 0, 0])

    result = IFFT(frequencies)

    print(result)


if __name__ == '__main__':
    main()
