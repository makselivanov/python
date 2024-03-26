import numpy as np

from src.mixin import RareMatrix


def main():
    np.random.seed(0)
    matrix_1 = RareMatrix(np.random.randint(0, 10, (10, 10)))
    matrix_2 = RareMatrix(np.random.randint(0, 10, (10, 10)))
    print(matrix_1)
    print(matrix_2)
    sum_matrix = matrix_1 + matrix_2
    sum_matrix.write("../artifacts/3.2/matrix+.txt")
    prod_matrix = matrix_1 * matrix_2
    prod_matrix.write("../artifacts/3.2/matrix*.txt")
    matprod_matrix = matrix_1 @ matrix_2
    matprod_matrix.write("../artifacts/3.2/matrix@.txt")


if __name__ == '__main__':
    main()
