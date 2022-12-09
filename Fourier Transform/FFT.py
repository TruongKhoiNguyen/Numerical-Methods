import numpy as np


def FFT(x: np.ndarray):
    N = x.size

    if N == 1:
        return x

    X_even = FFT(x[::2])
    X_odd = FFT(x[1::2])

    factor = np.exp(-2j*np.pi*np.arange(N) / N)

    X = np.concatenate([X_even + factor[:int(N/2)] * X_odd,
                       X_even + factor[int(N/2):] * X_odd])

    return X


def main():
    input_signal = np.array([4, 0, 3, 6, 2, 9, 6, 5])

    result = FFT(input_signal)

    print(result)


if __name__ == '__main__':
    main()
