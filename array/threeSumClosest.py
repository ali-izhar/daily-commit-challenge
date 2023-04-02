"""
Difficulty: Medium

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

Constraints:
    * 3 <= nums.length <= 500
    * -1000 <= nums[i] <= 1000
    * -10^4 <= target <= 10^4
"""

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        # temporary result
        res = sum(nums[:3])
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                # temporary sum
                s = nums[i] + nums[l] + nums[r]

                # update res if s is closer to target
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return res
        return res