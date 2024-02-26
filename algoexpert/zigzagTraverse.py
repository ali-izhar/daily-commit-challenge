"""
PROBLEM STATEMENT:

Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n == m) and returns a one-dimensional array of all the array's elements in zigzag order.

Zigzag order starts at the top left corner of the two-dimensional array, goes down by one element, and proceeds in a zigzag pattern all the way to the bottom right corner.

Sample Input:
array = [
    [1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12, 15],
    [7, 13, 14, 16]
]

Sample Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
"""

# Time: O(n) | Space: O(n)
def zigzagTraverse(array):
    rows, cols = len(array), len(array[0])
    
    # Handle edge case for a single-row array
    if rows == 1:
        return array[0]

    result = []
    row, col = 0, 0
    desc = True

    while row < rows and col < cols:
        diag = getDiagonal(array, row, col, desc)
        result.extend(diag)
        if row < rows - 1:
            row += 1
            desc = not desc
            continue
        row = rows - 1
        col += 1
        desc = not desc
    return result


def getDiagonal(array, row, col, desc):
    tempDiag = []
    while row >= 0 and row < len(array) and col < len(array[0]):
        tempDiag.append(array[row][col])
        row -= 1 
        col += 1
    if desc:
        tempDiag.reverse()
    return tempDiag


# Time: O(n) | Space: O(n)
def zigzagTraverse(array):
    height = len(array) - 1
    width = len(array[0]) - 1
    result = []
    row, col = 0, 0
    goingDown = True
    while not isOutOfBounds(row, col, height, width):
        result.append(array[row][col])
        if goingDown:
            if col == 0 or row == height:
                goingDown = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                goingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return result

def isOutOfBounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width