"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 
Constraints:
    * 1 <= s.length <= 10^4
    * s consists of parentheses only '()[]{}'
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                # if stack is empty, then there is no open bracket to match
                if len(stack) == 0:
                    return False
                if c == ")" and stack[-1] != "(":
                    return False
                if c == "]" and stack[-1] != "[":
                    return False
                if c == "}" and stack[-1] != "{":
                    return False
                stack.pop()
        return len(stack) == 0