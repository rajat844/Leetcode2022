# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return
        
        def isRoot(root):
            if root.left == None and root.right == None:
                return True
            
        
        def helper(root,Sum):
            
            Sum = Sum + root.val
            
            if isRoot(root):
                if Sum == targetSum:
                    return True
            else :
                if root.left:
                    if helper(root.left,Sum) == True:
                        return True
                if root.right:
                    if helper(root.right,Sum) == True:
                        return True
            return False
        
        return helper(root,0)