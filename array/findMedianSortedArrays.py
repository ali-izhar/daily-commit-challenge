"""
Difficulty: Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
Constraints:
    * nums1.length == m
    * nums2.length == n
    * 0 <= m <= 1000
    * 0 <= n <= 1000
    * 1 <= m + n <= 2000
    * -10^6 <= nums1[i], nums2[i] <= 10^6
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge and sort both lists
        merge = nums1.copy()
        merge.extend(nums2)
        merge.sort()

        # return the median of the merged list
        if len(merge) % 2 == 0:
            i, j = merge[len(merge) // 2], merge[len(merge) // 2 - 1]
            return (i + j) / 2
        else:
            return merge[len(merge) // 2]