# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        head = root
        ptr = None
        while root:
            if root.val > val:
                ptr = root
                root = root.left
            else:
                ptr = root
                root = root.right
        
        if ptr.val > val:
            ptr.left = TreeNode(val)
        else :
            ptr.right = TreeNode(val)
        
        return head