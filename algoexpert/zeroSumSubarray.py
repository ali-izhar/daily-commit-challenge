"""
PROBLEM STATEMENT:
You're given a list of integers `nums`. Write a function that returns a boolean representing whether there exists a zero-sum subarray of `nums`.

A zero-sum subarray is defined to be a subarray whose sum is 0. A subarray is a contiguous sequence of elements within the list.

Sample Input:
nums = [-5, -5, 2, 3, -2]

Sample Output:
True
"""

# Time: O(n^2) | Space: O(1)
def zeroSumSubarray(nums):
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum == 0:
                return True
    return False

# Time: O(n) | Space: O(n)
def zeroSumSubarray(nums):
    """Intuition:
    [-5, -5, 2, 3, -2]
    For each element, we calculate the sum of all elements from the beginning of the array to the current element. If the sum is already present in the set, then we have found a zero sum subarray.

    [-5, -5, 2, 3, -2]
    [-5, -10, -8, -5, -7]

    Since -5 is already present in the set, we have found a zero sum subarray - because we're back to the same sum we had before adding the current element.
    
    Note: We need to add 0 to the set to handle the case when the sum of all elements from the beginning of the array to the current element is 0.
    """
    sum = 0
    sumSet = set()
    for num in nums:
        sum += num
        if sum in sumSet or sum == 0:
            return True
        sumSet.add(sum)
    return False