class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n '.join(['\t '.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix([map(sum, zip(*t)) for t in zip(self.matrix, other.matrix)])

First_matrix = Matrix([[5, 9, 1, 7], [4, 8, 4, 5], [9, 12, 5, 1]])
Second_matrix = Matrix([[1, 5, 3, 2], [2, 7, 3, 2], [3, 5, 4, 1]])

print('Первая матрица:\n', First_matrix, end='\n\n')
print('Вторая матрица:\n', Second_matrix, end='\n\n')
print('Сумма матриц:\n', First_matrix + Second_matrix)