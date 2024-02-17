"""
PROBLEM STATEMENT:
Write a function that takes in an array of integers and returns the length of the longest peak in the array.

A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip (the highest value in the peak), at which point they become strictly decreasing. At least three integers are required to form a peak.

For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and neither do the integers 1, 2, 2, 0.

Note that the integers in the array do not need to be unique.

Sample Input:
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

Sample Output:
6 // 0, 10, 6, 5, -1, -3
"""

# Time: O(n) | Space: O(1)
def longestPeak(array):
    longestPeakLength = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue
        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1
        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1
        currentPeakLength = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        i = rightIdx
    return longestPeakLength

# Time: O(n) | Space: O(1)
def longestPeak(array):
    peaks = []
    n = len(array)
    for i in range(1, n - 1):
        if array[i - 1] < array[i] > array[i + 1]:
            peaks.append((i, array[i]))

    highest = []
    for peak in peaks:
        idx, val = peak

        left = idx - 2
        right = idx + 2

        while left >= 0 and array[left] < array[left + 1]:
            left -= 1
        while right < n and array[right] < array[right - 1]:
            right += 1

        highest.append(right - left - 1)

    return max(highest) if highest else 0
