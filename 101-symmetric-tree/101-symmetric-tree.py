# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(node1,node2):
            if node1 == None or node2 == None:
                return node1 == node2
            
            if node1.val == node2.val:
                return helper(node1.left,node2.right) and helper(node1.right,node2.left)
            
            return False
        
        return helper(root.left,root.right)
        
        
        