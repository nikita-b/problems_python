# Find the sum of all left leaves in a given binary tree.
# https://leetcode.com/problems/sum-of-left-leaves/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.sum = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        self.loop(root)

    def loop(self, root, left=False) -> None:
        if not root:
            return
        if left and not root.left and not root.right:
            self.sum += self.root.val
        self.loop(root.left, True)
        self.loop(root.right)