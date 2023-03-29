"""
Difficulty: Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
    * n == height.length
    * 2 <= n <= 10^5
    * 0 <= height[i] <= 10^4
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute force solution. Time complexity: O(n^2)
        maximum = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                base = j - i
                if height[i] <= height[j]:
                    product = base * height[i]
                else:
                    product = base * height[j]
                
                if product > maximum:
                    maximum = product
                
                # area = min(height[i], height[j]) * (j-i)
                # maximum = max(maximum, area)
        return maximum

    def maxArea(self, height: List[int]) -> int:
        # Two pointer solution. Time complexity: O(n)
        left = 0
        right = len(height) - 1
        maximum = 0
        while left < right:
            base = right - left
            if height[left] <= height[right]:
                product = base * height[left]
                left += 1
            else:
                product = base * height[right]
                right -= 1
            maximum = max(maximum, product)
    
        return maximum