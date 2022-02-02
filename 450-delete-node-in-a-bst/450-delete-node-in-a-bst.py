# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLastRight(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.right is None:
            return root
        return self.findLastRight(root.right)
    
    def helper(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        
        rightchild = root.right
        lastright = self.findLastRight(root.left)
        lastright.right = rightchild
        return root.left
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if root.val == key:
            return self.helper(root)
        head = root
        
        while root:
            if root.val > key:
                if root.left is not None and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right is not None and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right
                    
        return head