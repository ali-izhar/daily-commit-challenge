"""
PROBLEM STATEMENT:
You walk into a theatre you're about to see a show in. The usher within the theatre walks you to your row and mentions you're allowed to sit anywhere within the given row. Naturally you'd like to sit in the seat that gives you the most space. You also would prefer this space to be evenly distributed on either side of you (e.g. if there are three empty seats in a row, you would prefer to sit in the middle of those three seats).

Given the theatre row represented as an integer array, return the seat index of where you should sit. Ones represent occupied seats and zeroes represent empty seats.

You may assume that someone is always sitting in the first and last seat of the row. Whenever there are two equally good seats, you should sit in the seat with the lower index. If there is no seat to sit in, return -1. The given array will always have a length of at least one and contain only ones and zeroes.

Sample Input:
row = [1, 0, 1, 0, 0, 0, 1]

Sample Output:
4
"""

# Time: O(n) | Space: O(1)
def bestSeat(row):
    maxDistance = -1
    bestSeat = -1
    for i in range(len(row)):
        if row[i] == 0:
            left = i - 1
            right = i + 1
            while left >= 0 and row[left] == 0:
                left -= 1
            while right < len(row) and row[right] == 0:
                right += 1
            leftDistance = i - left
            rightDistance = right - i
            minDistance = min(leftDistance, rightDistance)
            if minDistance > maxDistance:
                maxDistance = minDistance
                bestSeat = i
    return bestSeat

# Time: O(n) | Space: O(1)
def bestSeat(row):
    maxDistance = -1
    bestSeat = -1
    for i in range(len(row)):
        if row[i] == 0:
            left = i - 1
            right = i + 1
            while left >= 0 and row[left] == 0:
                left -= 1
            while right < len(row) and row[right] == 0:
                right += 1
            leftDistance = i - left
            rightDistance = right - i
            minDistance = min(leftDistance, rightDistance)
            if minDistance > maxDistance:
                maxDistance = minDistance
                bestSeat = i
            elif minDistance == maxDistance:
                bestSeat = min(bestSeat, i)
    return bestSeat