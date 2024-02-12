"""
PROBLEM STATEMENT:
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array. Assume that there will be at most one pair of numbers summing up to the target sum.

Sample Input:
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

Sample Output:
[-1, 11]
"""

# Method 1: Using two for loops
# Time: O(n^2) | Space: O(1)
def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []


# Method 2: Using a hash table
# Time: O(n) | Space: O(n)
def twoNumberSum(array, targetSum):
    dict = {}
    for num in array:
        complement = targetSum - num
        if complement in dict:
            return [complement, num]
        else:
            dict[num] = True
    return []


# Method 3: Using two pointers
# Time: O(nlogn) | Space: O(1)
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []