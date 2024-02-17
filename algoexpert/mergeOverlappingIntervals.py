"""
PROBLEM STATEMENT:
Write a function that takes in a non-empty list of arbitrary intervals, merges any overlapping intervals, and returns the new intervals in no particular order.

An interval is an array of two integers, with interval[0] as the start of the interval and interval[1] as the end of the interval.

Note that back-to-back intervals aren't considered to be overlapping. For example, [1, 5] and [6, 7] aren't overlapping; however, [1, 6] and [6, 7] are indeed overlapping.

Also note that the start of any particular interval will always be less than or equal to the end of that interval.

Sample Input:
intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]

Sample Output:
[[1, 2], [3, 8], [9, 10]]
"""

# Time: O(nlogn) | Space: O(n)
def mergeOverlappingIntervals(intervals):
    # sort the intervals based on the start time
    intervals = sorted(intervals, key=lambda x: x[0])
    results = [intervals[0]]

    for i in range(1, len(intervals)):
        curr_start, curr_end = intervals[i]
        _, prev_end = results[-1]

        if curr_start > prev_end:
            results.append(intervals[i])
        else:
            if curr_end > prev_end:
                results[-1][1] = curr_end
    return results


# Time: O(nlogn) | Space: O(n)
def mergeOverlappingIntervals(intervals):
    # sort the intervals based on the start time
    intervals = sorted(intervals, key=lambda x: x[0])
    mergedIntervals = []
    currentInterval = intervals[0]
    mergedIntervals.append(currentInterval)
    for nextInterval in intervals:
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval
        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            currentInterval = nextInterval
            mergedIntervals.append(currentInterval)
    return mergedIntervals