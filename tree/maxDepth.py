"""
Difficulty: Easy

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
    * The number of nodes in the tree is in the range [0, 10^4].
    * -100 <= Node.val <= 100
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # solution 1
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    # solution 2 
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        left = 0
        right = 0

        if root.left:
            left = 1 + self.maxDepth(root.left)
        
        if root.right:
            right = 1 + self.maxDepth(root.right)
        
        return max(left, right)