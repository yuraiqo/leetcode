from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return (True, 0)
            left_b, left_d = helper(root.left)
            right_b, right_d = helper(root.right)
            balanced = left_b and right_b and abs(left_d - right_d) <= 1
            return (balanced, 1 + max(left_d, right_d))
        result, _ = helper(root)
        return result
