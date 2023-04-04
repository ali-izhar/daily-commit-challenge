"""
Difficulty: Medium

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
    * 0 <= nums.length <= 10^5
    * -10^9 <= nums[i] <= 10^9
    * nums is a non-decreasing array.
    * -10^9 <= target <= 10^9
"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Find the leftmost index
        left = self.findLeft(nums, target)
        
        # If the target is not in the array, return [-1, -1]
        if left == -1:
            return [-1, -1]
        
        # Find the rightmost index
        right = self.findRight(nums, target)
        
        return [left, right]
    
    def findLeft(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def findRight(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1