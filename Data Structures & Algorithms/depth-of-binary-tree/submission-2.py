# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def d(n):
            if not n: return 0
            leftdepth = d(n.left)
            rightdepth = d(n.right)
            return 1 + max(leftdepth, rightdepth)
        return d(root)

