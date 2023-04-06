"""
Difficulty: Hard

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and
i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
    * 1 <= nums.length <= 10^4
    * 0 <= nums[i] <= 1000
    * It's guaranteed that you can reach nums[n - 1].
"""

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] >= n - 1:
            return 1
        if nums[0] == 0:
            return -1
        max_reach = nums[0]
        steps = nums[0]
        jumps = 1
        for i in range(1, n):
            if i == n - 1:
                return jumps
            max_reach = max(max_reach, i + nums[i])
            steps -= 1
            if steps == 0:
                jumps += 1
                if i >= max_reach:
                    return -1
                steps = max_reach - i
        return -1