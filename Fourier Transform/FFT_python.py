import numpy as np


def main():
    input_signal = np.array([4, 0, 3, 6, 2, 9, 6, 5])

    result = np.fft.fft(input_signal)

    print(result)


if __name__ == '__main__':
    main()
