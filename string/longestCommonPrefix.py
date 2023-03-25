"""
Difficulty: Easy

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:
    * 1 <= strs.length <= 200
    * 0 <= strs[i].length <= 200
    * strs[i] consists of only lowercase English letters.
"""

from typing import List

class Solution:

    # approach 1: horizontal scanning
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        ans = strs[0]

        m = 0
        # Loop through the remaining strings in the list.
        for i in strs[1:]:
            # If the current string is empty, there can be no common prefix.
            if len(i) == 0:
                return ""

            for k, c in enumerate(i):
                # try-catch to prevent index out of bounds for uneven length strings
                try:
                    if c == ans[k]:
                        m += 1
                    else:
                        break
                except:
                    break
            ans = ans[:m]
            m = 0
        return ans


    # approach 2: vertical scanning
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix