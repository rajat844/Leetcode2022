# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal ans
            if node is None:
                return 0
            lh = max(0,helper(node.left))
            rh = max(0,helper(node.right))
            
            ans = max(node.val+lh+rh,ans)
            
            return node.val+max(lh,rh)
        
        ans = -math.inf
        helper(root)
        return ans
        