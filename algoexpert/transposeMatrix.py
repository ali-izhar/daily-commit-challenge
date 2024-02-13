"""
PROBLEM STATEMENT:
You're given a 2D array of integers `matrix`. Write a function that returns the transpose of `matrix`. The transpose of a matrix is obtained by exchanging the rows and columns of the matrix. You can assume that the input matrix is non-empty.

Sample Input
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

Sample Output
[
    [1, 4],
    [2, 5],
    [3, 6],
]
"""

# Time: O(n*m) | Space: O(n*m)
def transposeMatrix(matrix):
    """Scan the matrix in row-major order. Add each row as a column in the transposed matrix."""
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


# Time: O(n*m) | Space: O(n*m)
def transposeMatrix(matrix):
    """Scan the matrix in column-major order. Add each column as a row in the transposed matrix."""
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []

    for j in range(cols):
        newRow = []
        for i in range(rows):
            newRow.append(matrix[i][j])
        transposed.append(newRow)
    return transposed
