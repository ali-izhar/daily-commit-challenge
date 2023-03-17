"""
Difficulty: Easy

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
 
Constraints:
    * -2^31 <= x <= 2^31 - 1
"""

class Solution:

    # approach 1: divide by 10, get remainder, add to result
    def reverse(self, x: int) -> int:
        result = ""
        y = abs(x)
        while y > 0:
            quot, rem = y // 10, y % 10
            result += str(rem)
            y = quot
        
        if not result:
            return 0
        
        result = int(result)
        if result < (-2**31) or result > (2**31 - 1):
            return 0

        if x < 0:
            result = -1 * result
        return result


    # approach 2: convert to string, reverse, convert back to int
    def reverse(self, x: int) -> int:
        if x < 0:
            return -1 * int(str(x)[1:][::-1])
        else:
            return int(str(x)[::-1])