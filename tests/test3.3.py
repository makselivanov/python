import numpy as np

from src.matrix import Matrix, Cache_clear


def main():
    np.random.seed(0)
    a_matrix = Matrix([[2, 3], [1, 4]])
    b_matrix = Matrix([[0, 1], [1, 0]])
    c_matrix = Matrix([[1, 2], [5, 2]])
    d_matrix = b_matrix
    base_path = "../artifacts/3.3/"
    assert hash(a_matrix) == hash(c_matrix) and (a_matrix != c_matrix) and (b_matrix == d_matrix)
    with open(base_path + "A.txt", "w") as A_file:
        A_file.write(str(a_matrix))
    with open(base_path + "B.txt", "w") as B_file:
        B_file.write(str(b_matrix))
    with open(base_path + "C.txt", "w") as C_file:
        C_file.write(str(c_matrix))
    with open(base_path + "D.txt", "w") as D_file:
        D_file.write(str(d_matrix))
    with open(base_path + "AB.txt", "w") as AB_file:
        AB_file.write(str(a_matrix @ b_matrix))
    Cache_clear()
    with open(base_path + "CD.txt", "w") as CD_file:
        CD_file.write(str(c_matrix @ d_matrix))
    with open(base_path + "hash.txt", "w") as hash_file:
        hash_file.write(str(hash(a_matrix @ b_matrix)))
        hash_file.write("\n")
        Cache_clear()
        hash_file.write(str(hash(c_matrix @ d_matrix)))


if __name__ == '__main__':
    main()
