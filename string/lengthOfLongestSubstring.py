"""
Difficulty: Medium

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:
    * 0 <= s.length <= 5 * 10^4
    * s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # try two-pointer approach        
        # dictionary to keep track of seen values
        seen = {}

        # start left point at zero
        left = 0

        # output variable
        maximum = 0

        for right in range(len(s)):
            if s[right] not in seen:
                maximum = max(maximum, right - left + 1)
            else:
                """
                There are 2 cases if s[right] is seen before:
                case1: s[right] is inside the current window, move the left pointer.
                case2: s[right] is not inside the current window, continue
                """
                # since left = right = 0, we need to check for equality as well
                if seen[s[right]] >= left:
                    left = seen[s[right]] + 1
                else:
                    maximum = max(maximum, right - left + 1)
                
            # now s[right] is seen
            seen[s[right]] = right
        return maximum