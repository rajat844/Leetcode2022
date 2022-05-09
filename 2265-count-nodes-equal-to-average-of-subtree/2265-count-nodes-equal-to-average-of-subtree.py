# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal ans
            if node == None:
                return 0,0
            
            lc,ls = helper(node.left)
            rc,rs = helper(node.right)
            
            if (ls + rs + node.val)//(lc + rc + 1) == node.val :
                    ans += 1
                    
            return lc+rc+1,ls+rs+node.val
        
        ans = 0
        cnt,sm = helper(root)
        return ans
        