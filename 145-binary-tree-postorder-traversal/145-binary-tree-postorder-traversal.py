# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []
        
        def helper(node):
            if node is None:
                return
            
            helper(node.left)
            helper(node.right)
            postorder.append(node.val)
        
        helper(root)
        return postorder