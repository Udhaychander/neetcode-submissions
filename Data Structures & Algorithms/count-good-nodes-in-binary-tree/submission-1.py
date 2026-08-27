# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res=0
        def a(n,m):
            if not n: return 0
            if n.val>=m:
                self.res+=1
            a(n.left,m)
            a(n.right,m)
        a(root,root.val)
        return self.res
            