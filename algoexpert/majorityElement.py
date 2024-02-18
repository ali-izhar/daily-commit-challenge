"""
PROBLEM STATEMENT:
Write a function that takes in a non-empty, unordered array of integers and returns the array's majority element without sorting the array and without using more than constant space.

An array's majority element is an element of the array that appears in over half of its indices. Note that the most common element in the array is not guaranteed to be the majority element. For example, consider the array [1, 2, 1, 1, 3, 4, 0]. The most common element in the array is 1, and it appears in three of the array's indices, but 1 is not the majority element because it doesn't appear in more than half of the array's indices.

You can assume that there will always be a majority element in the array.

Sample Input:
array = [1, 2, 3, 2, 2, 1, 2]

Sample Output:
2 // 2 occurs in 4/7 array indices, making it the majority element
"""

# Time: O(n) | Space: O(n)
def majorityElement(array):
    freq = {}
    for i in array:
        freq[i] = freq.get(i, 0) + 1
    return max(freq, key=freq.get)


# Time: O(n) | Space: O(1)
def majorityElement(array):
    """Intuition:
    - We can use the Boyer-Moore Voting Algorithm to solve this
    - The algorithm works by keeping track of a candidate and a counter
    - The candidate is the majority element, and the counter is the number of times it appears
    - We iterate through the array and update the candidate and counter based on the current element
    - If the current element is the same as the candidate, we increment the counter
    - If the current element is different from the candidate, we decrement the counter
    - If the counter reaches 0, we update the candidate to the current element and set the counter to 1
    - At the end, the candidate will be the majority element
    """
    candidate = array[0]
    counter = 1
    for i in range(1, len(array)):
        if array[i] == candidate:
            counter += 1
        else:
            counter -= 1
            if counter == -1:
                candidate = array[i]
                counter = 1
    return candidate