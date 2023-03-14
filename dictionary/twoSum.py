"""
Difficulty: Easy

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
    *    2 <= nums.length <= 10^4
    *   -10^9 <= nums[i] <= 10^9
    *   -10^9 <= target <= 10^9
    *   Only one valid answer exists.
"""

class Solution:
    
    """
    Approach 1: Brute Force
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    """
    Approach 2: Dictionary
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, j in enumerate(nums):
            # get the complement of the current element
            comp = target - j

            # if complement exists in dictionary,
            # return the index of the complement and the current index
            # otherwise, add the current element to the dictionary
            if comp in d:
                return [d[comp], i]
            d[j] = i