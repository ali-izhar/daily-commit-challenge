"""
Difficulty: Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
    * 3 <= nums.length <= 3000
    * -10^5 <= nums[i] <= 10^5
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Sort the array so that we can skip duplicates
        nums.sort()
        result = []
        for i in range(len(nums) - 2):

            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find the remaining two numbers
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # If the total is less than zero, we need a larger number to get closer to zero so we go right (increase left)
                if total < 0:
                    left += 1

                # If the total is greater than zero, we need a smaller number to get closer to zero so we go left (decrease right)
                elif total > 0:
                    right -= 1
                
                # If the total is zero, we found a triplet
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # we could use an if-statement here to check if left < right. If yes, increment left 
                    # However, we can use a while-loop to skip duplicates.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # if the next number in the right is the same as the current number, we need to skip it
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # if no duplicates were found, we can increment left and decrement right
                    left += 1
                    right -= 1

        return result