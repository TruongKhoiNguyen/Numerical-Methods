class DataPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# function to interpolate the given data points
# using Lagrange's formula
# xi -> corresponds to the new data point
# whose value is to be obtained
# n -> represents the number of known data points
def interpolate(f: list, xi: float, n: int) -> float:

    # Initialize result
    result = 0.0
    for i in range(n):

        # Compute individual terms of above formula
        term = f[i].y
        for j in range(n):
            if j != i:
                term = term * (xi - f[j].x) / (f[i].x - f[j].x)

        # Add current term to result
        result += term

    return result


def main():
    # Get input
    data_points: list[DataPoint] = []

    n = input('Get the number of data points: ')
    n = int(n)

    for i in range(n):
        x_tmp = input(f'x{i} = ')
        x_tmp = float(x_tmp)

        f_tmp = input(f'f{i} = ')
        f_tmp = float(f_tmp)

        data_points.append(DataPoint(x_tmp, f_tmp))

    cal_input = input('Get x you want to calculate: ')
    cal_input = float(cal_input)

    # Print input (This is used for testing purpose)
    for i in range(n):
        print(f'({data_points[i].x}, {data_points[i].y})')

    # Calculate
    result = interpolate(data_points, cal_input, n)

    # Print output
    print(f'The value of f({cal_input}) is {result}')


if __name__ == '__main__':
    main()
