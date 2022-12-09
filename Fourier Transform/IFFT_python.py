import numpy as np
from numpy.fft import ifft


def main():
    frequencies = np.array([0, 0, 0, 0, 8, 0, 0, 0])

    result = ifft(frequencies)

    print(result)


if __name__ == '__main__':
    main()
