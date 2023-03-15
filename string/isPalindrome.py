"""
Difficulty: Easy

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
    * -2^31 <= x <= 2^31 - 1
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    

    # Can you solve it without converting the integer to a string?
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        # reverse the number
        rev = 0
        num = x
        while num > 0:
            rev = rev * 10 + num % 10
            num = num // 10
        return x == rev