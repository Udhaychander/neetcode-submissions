# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(left, node, right):
            if not node:
                return True
            if (left < node.val < right):
                pass
            else:
                return False
            left= valid(left, node.left, node.val)
            right= valid(node.val, node.right, right)
            return left and right
        return valid(float("-inf"), root, float("inf"))