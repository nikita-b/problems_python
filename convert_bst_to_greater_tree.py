# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

# As a reminder, a binary search tree is a tree that satisfies these constraints:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# https://leetcode.com/problems/convert-bst-to-greater-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

a = TreeNode(8)
b = TreeNode(7, None, a)
d = TreeNode(5)
c = TreeNode(6, d, b)
j = TreeNode(3)
k = TreeNode(2, None, j)
z = TreeNode(0)
o = TreeNode(1, z, k)
e = TreeNode(4, o, c)

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traversal(root, result):
            if root.right is not None:
                result = traversal(root.right, result)
            result += root.val
            root.val = result
            if root.left is not None:
                result = traversal(root.left, result)

            return result
        if root is None:
            return root

        traversal(root, 0)
        return root
