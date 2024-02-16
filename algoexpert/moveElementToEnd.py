"""
PROBLEM STATEMENT:
You're given an array of integers and an integer. Write a function that moves all instances of that integer in the array to the end of the array and returns the array.

The function should perform this in place and does not need to maintain the order of the other integers.

Sample Input:
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

Sample Output:
[1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4 could be ordered differently
"""

# Time: O(n) | Space: O(1)
def moveElementToEnd(array, toMove):
    left = 0
    right = len(array) - 1
    while left < right:
        while left < right and array[right] == toMove:
            right -= 1
        if array[left] == toMove:
            array[left], array[right] = array[right], array[left]
        left += 1
    return array


# Time: O(n) | Space: O(1)
def moveElementToEnd(array, toMove):
    left = 0
    right = 1
    while right < len(array):
        left_value = array[left]
        right_value = array[right]

        if right_value == toMove:
            right += 1
        elif left_value != toMove and right_value != toMove:
            left += 1
            right += 1
        else:
            if right != len(array):
                array[left], array[right] = array[right], array[left]
                left += 1
                right += 1

    return array