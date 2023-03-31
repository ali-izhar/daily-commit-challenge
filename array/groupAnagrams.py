"""
Difficulty: Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
    * 1 <= strs.length <= 10^4
    * 0 <= strs[i].length <= 100
    * strs[i] consists of lowercase English letters.
"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = {}
        for s in strs:
            # why tuple? because it's hashable. only hashable objects can be used as keys in a dictionary
            # sorted() returns a list, so we need to convert it to a tuple
            key = tuple(sorted(s))
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        for k in d:
            res.append(d[k])
        return res