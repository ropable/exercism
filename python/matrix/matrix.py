class Matrix:
    def __init__(self, matrix_string: str):
        # Split matrix_string into lines, split lines on whitespace and cast elements as integers.
        self.matrix = [[int(j) for j in i.split()] for i in matrix_string.splitlines()]

    def row(self, index: int) -> list[int]:
        return self.matrix[index - 1]

    def column(self, index: int) -> list[int]:
        return [i[index - 1] for i in self.matrix]
