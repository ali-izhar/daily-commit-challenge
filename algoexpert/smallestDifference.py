"""
PROBLEM STATEMENT:
Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position.

Note that the absolute difference of two integers is the distance between them on the real number line. For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.

You can assume that there will only be one pair of numbers with the smallest difference.

Sample Input:
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

Sample Output:
[28, 26]
"""

# Time: O(nlog(n) + mlog(m)) | Space: O(1)
# where n is the length of arrayOne and m is the length of arrayTwo
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    
    smallest = float("inf")
    i, j = 0, 0
    smallestPair = []

    while i < len(arrayOne) and j < len(arrayTwo):
        left_value = arrayOne[i]
        right_value = arrayTwo[j]
        diff = abs(left_value - right_value)

        if diff < smallest:
            smallest = diff
            smallestPair = [left_value, right_value]

        if left_value < right_value:
            i += 1
        elif right_value < left_value:
            j += 1
        else:
            return [left_value, right_value]
        
    return smallestPair