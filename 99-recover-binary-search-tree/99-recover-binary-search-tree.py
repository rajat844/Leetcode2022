# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def __init__(self):
        self.first = None
        self.prev = TreeNode(-math.inf)
        self.middle = None
        self.last = None
        
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        if self.prev and root.val < self.prev.val:
            if self.first is None:
                self.first = self.prev
                self.middle = root
            else :
                self.last = root
        self.prev = root
        self.inorder(root.right)
            
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        if self.last and self.first:
            self.first.val ,self.last.val = self.last.val ,self.first.val
        else :
            self.first.val,self.middle.val = self.middle.val ,self.first.val