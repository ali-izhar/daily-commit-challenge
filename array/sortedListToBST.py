"""
Difficulty: Medium

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5]

"""

from typing import Optional
from linkedList import ListNode

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        # find middle element as root
        mid = self.findMiddle(head)
        root = TreeNode(mid.val)
        
        if head == mid:
            return root
        
        # recursively build using left and right subarrays
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        
        return root
    
    def findMiddle(self, head: ListNode) -> ListNode:
        prevPtr = None
        slowPtr = head
        fastPtr = head
        
        while fastPtr and fastPtr.next:
            prevPtr = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        
        if prevPtr:
            prevPtr.next = None
        
        return slowPtr