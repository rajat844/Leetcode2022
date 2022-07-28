# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node,s):
            nonlocal ans
            if node.left is None and node.right is None:
                s += str(node.val)
                ans += int(s)
                return
            if node.left:
                helper(node.left,s +str(node.val))
            if node.right:
                helper(node.right,s +str(node.val))   
             
        ans = 0
        helper(root,"")
        return ans
        
            
        