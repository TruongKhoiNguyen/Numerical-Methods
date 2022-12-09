import numpy as np
from scipy.interpolate import CubicSpline


def main():
    x = np.arange(5)
    y = np.array([21, 24, 24, 18, 16])

    cp = CubicSpline(x, y)

    print(cp(3))


if __name__ == '__main__':
    main()
