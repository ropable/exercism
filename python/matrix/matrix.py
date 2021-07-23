from typing import Text, List


class Matrix:
    def __init__(self, matrix_string: Text):
        # Split matrix_string into lines, split lines on whitespace and cast elements as integers.
        self.matrix = [[int(j) for j in i.split()] for i in matrix_string.splitlines()]

    def row(self, index: int) -> List:
        return self.matrix[index - 1]

    def column(self, index: int) -> List:
        return [i[index - 1] for i in self.matrix]
