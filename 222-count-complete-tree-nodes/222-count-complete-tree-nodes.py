# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def heightLeft(node):
            height = 0
            while node:
                height += 1
                node = node.left
            
            return height
        
        def heightRight(node):
            height = 0
            while node:
                height += 1
                node = node.right
            
            return height
                
        
        def helper(node):
            if node is None:
                return 0
            lh = heightLeft(node)
            rh = heightRight(node)
            
            if lh == rh:
                return (2**lh - 1)
            else:
                return 1 + helper(node.left)+helper(node.right)
        
        return helper(root)