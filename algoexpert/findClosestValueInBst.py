"""
PROBLEM STATEMENT:
Write a function that takes in a Binary Search Tree (BST) and a target integer value and returns the closest value to that target value contained in the BST.

You can assume that there will only be one closest value.

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null.

Sample Input:
tree =   10
       /     \
      5      15
    /   \   /    \
   2     5 13    22
 /          \
1           14

target = 12

Sample Output:
13
"""

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Time: O(log(n)) | Space: O(1)
def findClosestValueInBst(tree, target):
    closest = float("inf")
    current = tree
    while current is not None:
        if abs(target - closest) > abs(target - current.value):
            closest = current.value
        if target < current.value:
            current = current.left
        elif target > current.value:
            current = current.right
        else:
            break
    return closest


# Time: O(log(n)) | Space: O(log(n))
def findClosestValueInBst(tree, target):
    return findClosestHelper(tree, target, float('inf'), None)

def findClosestHelper(tree, target, min_dist, best_value):
    if not tree:
        return best_value

    curr_dist = abs(target - tree.value)
    if curr_dist < min_dist:
        min_dist = curr_dist
        best_value = tree.value

    if target < tree.value and tree.left is not None:
        return findClosestHelper(tree.left, target, min_dist, best_value)
    elif target > tree.value and tree.right is not None:
        return findClosestHelper(tree.right, target, min_dist, best_value)
    else:
        return best_value

