# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def heightleft (self, root: Optional[TreeNode]) ->int:
        height = 0
        while(root):
            height += 1
            root = root.left
        return height
    
    def heightright (self, root: Optional[TreeNode]) ->int:
        height = 0
        while root:
            height += 1
            root = root.right
        return height
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        
        lh = self.heightleft(root)
        rh = self.heightright(root)
        
        if lh == rh:
            return ((1<<lh)-1)
        
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
        