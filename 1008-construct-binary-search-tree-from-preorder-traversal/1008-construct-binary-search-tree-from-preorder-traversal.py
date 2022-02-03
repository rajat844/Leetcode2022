# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(upperbound):
            nonlocal i
            if i == n or preorder[i] >= upperbound:
                return None
            
            root = TreeNode(preorder[i])
            i += 1
            root.left = helper(root.val)
            root.right = helper(upperbound)
            return root
        upperbound = math.inf
        i = 0
        n = len(preorder)
        return helper(upperbound)
        
        