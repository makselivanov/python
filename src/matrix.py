import numpy as np


class HashMatrixMixin:
    def __hash__(self):
        return sum([sum(row) for row in self.matrix])


_cache = dict()


def Cache_clear():
    _cache.clear()


class Matrix(HashMatrixMixin):
    """Common Matrix"""
    n: int
    m: int
    matrix: list[list[float]]

    def __init__(self, matrix: list[list[float]] | np.ndarray):
        self.matrix = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])
        if not all(map(lambda row: len(row) == self.m, matrix)):
            raise ValueError("__init__ got not a matrix")

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("__add__ other is not a matrix")
        if self.n != other.n or self.m != other.m:
            raise ValueError("__add__ got different matrix's")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.m)] for i in range(self.n)]
        return Matrix(result)

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("__mul__ other is not a matrix")
        if self.n != other.n or self.m != other.m:
            raise ValueError("__mul__ got different matrix's")
        result = [[self.matrix[i][j] * other.matrix[i][j] for j in range(self.m)] for i in range(self.n)]
        return Matrix(result)

    def __matmul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("__matmul__ other is not a matrix")
        if self.m != other.n:
            raise ValueError("__matmul__ got incorrect shapes")
        hash_1 = hash(self)
        hash_2 = hash(other)
        if (hash_1, hash_2) not in _cache:
            result = [[sum([self.matrix[i][k] * other.matrix[k][j] for k in range(self.m)]) for j in range(other.m)] for i in range(self.n)]
            _cache[(hash_1, hash_2)] = Matrix(result)
        return _cache[(hash_1, hash_2)]

    def __str__(self):
        return str(self.matrix)