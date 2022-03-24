# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def helper(node):
            nonlocal k
            nonlocal res
            if node is None:
                return
            helper(node.left)
            k -= 1
            if k == 0:
                res = node.val
            helper(node.right)
            
        res = 0
        helper(root)
        return res