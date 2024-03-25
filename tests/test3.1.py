import numpy as np

from src.matrix import Matrix


def main():
    np.random.seed(0)
    matrix_1 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix_2 = Matrix(np.random.randint(0, 10, (10, 10)))
    with open("../artifacts/3.1/matrix+.txt", "w") as sum_file:
        result = matrix_1 + matrix_2
        sum_file.write(str(result))
    with open("../artifacts/3.1/matrix*.txt", "w") as mult_file:
        result = matrix_1 * matrix_2
        mult_file.write(str(result))
    with open("../artifacts/3.1/matrix@.txt", "w") as matmul_file:
        result = matrix_1 @ matrix_2
        matmul_file.write(str(result))


if __name__ == '__main__':
    main()
