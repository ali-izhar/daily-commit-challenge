"""
PROBLEM STATEMENT:
Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an array and the array itself are both valid subsequences of the array.

Sample Input:
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

Sample Output:
True

APPROACH:
- Initialize two pointers, one for each array
- Iterate through the first array
- If the value at the first array is equal to the value at the second array, increment the second pointer
- If the second pointer is equal to the length of the second array, return True
- If the loop ends, return False
- Time: O(n) | Space: O(1)
"""

# Time: O(n) | Space: O(1)
def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)

# Time: O(n) | Space: O(1)
def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)
