# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root: Optional[TreeNode]):
        if root is None:
            return 
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = list()
        self.inorder(root)
        
        for i in range(1,len(self.res)):
            if self.res[i-1] >= self.res[i]:
                return False
        return True
        