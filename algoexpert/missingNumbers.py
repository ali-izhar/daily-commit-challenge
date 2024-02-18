"""
PROBLEM STATEMENT:
You're given an unordered list of unique integers 'nums' in the range [1, n], where n represents the length of 'nums' + 2. This means that the two numbers in the range are missing from the list. Write a function that returns the two missing numbers in the list.
"""

# Time: O(n) | Space: O(n)
def missingNumbers(nums):
    result = []
    numsSet = set(nums)
    for i in range(1, len(nums) + 3):
        if i not in numsSet:
            result.append(i)
    return result

# Time: O(n) | Space: O(1)
def missingNumbers(nums):
    total = sum(range(1, len(nums) + 3))
    for num in nums:
        total -= num

    averageMissingValue = total // 2
    foundFirstHalf = 0
    foundSecondHalf = 0

    for num in nums:
        if num <= averageMissingValue:
            foundFirstHalf += num
        else:
            foundSecondHalf += num

    actualFirstHalf = sum(range(1, averageMissingValue + 1))
    actualSecondHalf = sum(range(averageMissingValue + 1, len(nums) + 3))

    return [actualFirstHalf - foundFirstHalf, actualSecondHalf - foundSecondHalf]