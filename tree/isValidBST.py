"""
Difficulty: Medium

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
    * The left subtree of a node contains only nodes with keys less than the node's key.
    * The right subtree of a node contains only nodes with keys greater than the node's key.
    * Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
    * The number of nodes in the tree is in the range [1, 10^4].
    * -2^31 <= Node.val <= 2^31 - 1
"""

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(node: TreeNode, lower: int, upper: int) -> bool:
            if node is None:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)

        return helper(root, float('-inf'), float('inf'))