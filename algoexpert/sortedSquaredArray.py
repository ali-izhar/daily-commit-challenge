"""
PROBLEM STATEMENT:
Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order.

Sample Input:
array = [-7, -3, 1, 9, 22, 30]

Sample Output:
[1, 9, 49, 81, 484, 900]
"""

# Time: O(nlogn) | Space: O(n)
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]

    for idx in range(len(array)):
        value = array[idx]
        sortedSquares[idx] = value ** 2

    sortedSquares.sort()
    return sortedSquares


# Time: O(n) | Space: O(n)
def sortedSquaredArray(array):
    result = []

    left = 0
    right = len(array) - 1

    while left <= right:
        left_sq = array[left] ** 2
        right_sq = array[right] ** 2

        if left_sq > right_sq:
            result.append(left_sq)
            left += 1
        else:
            result.append(right_sq)
            right -= 1

    return result[::-1]


# Time: O(n) | Space: O(n)
def sortedSquaredArray(array):
    result = [0 for _ in array]

    left = 0
    right = len(array) - 1

    for idx in reversed(range(len(array))):
        left_val = array[left]
        right_val = array[right]

        if abs(left_val) > abs(right_val):
            result[idx] = left_val ** 2
            left += 1
        else:
            result[idx] = right_val ** 2
            right -= 1

    return result