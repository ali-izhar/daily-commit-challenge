"""
PROBLEM STATEMENT:
Write a function that takes in a non-empty array of integers and returns an array of the same length, where each element in the output array is equal to the product of every other number in the input array.

In other words, the value at output[i] is equal to the product of every number in the input array other than input[i].

Note that you're expected to solve this problem without using division.

Sample Input:
array = [5, 1, 4, 2]

Sample Output:
[8, 40, 10, 20]
"""

# Time: O(n^2) | Space: O(n)
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    for i in range(len(array)):
        runningProduct = 1
        for j in range(len(array)):
            if i != j:
                runningProduct *= array[j]
        products[i] = runningProduct
    return products


# Time: O(n) | Space: O(n)
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    leftProducts = [1 for _ in range(len(array))]
    rightProducts = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(array)):
        leftProducts[i] = leftRunningProduct
        leftRunningProduct *= array[i]
    
    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        rightProducts[i] = rightRunningProduct
        rightRunningProduct *= array[i]
    
    for i in range(len(array)):
        products[i] = leftProducts[i] * rightProducts[i]
    
    return products


# Time: O(n) | Space: O(n)
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]
    
    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]
    
    return products