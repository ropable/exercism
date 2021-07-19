class Matrix:
    def __init__(self, matrix_string):
        # Parse matrix_string in two steps, for readability.
        split_string = [s.split(" ") for s in matrix_string.splitlines()]
        # Cast matrix elements as integers.
        self.matrix = [[int(y) for y in x] for x in split_string]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [i[index - 1] for i in self.matrix]
