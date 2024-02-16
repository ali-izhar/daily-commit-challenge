"""
PROBLEM STATEMENT:
Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.

Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.

Note that empty arrays and arrays of one element are monotonic.

Sample Input:
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

Sample Output:
True
"""

# Time: O(n) | Space: O(1)
def isMonotonic(array):
    if len(array) <= 2:
        return True
    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue
        if breaksDirection(direction, array[i - 1], array[i]):
            return False
    return True

def breaksDirection(direction, previousInt, currentInt):
    difference = currentInt - previousInt
    if direction > 0:
        return difference < 0
    return difference > 0


# Time: O(n) | Space: O(1)
def isMonotonic(array):
    isNonIncreasing = True
    isNonDecreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isNonIncreasing = False
        if array[i] > array[i - 1]:
            isNonDecreasing = False
    return isNonIncreasing or isNonDecreasing


# Time: O(n) | Space: O(1)
def isMonotonic(array):
    nonIncreasing = True
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            nonIncreasing = False
            break

    if nonIncreasing:
        return True
    
    nonDecreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            nonDecreasing = False
            break

    return nonDecreasing