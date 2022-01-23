# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def helper(root,ans):
            if root is None:
                return
            
            ans.append(root.val)
            helper(root.left,ans)
            helper(root.right,ans)
            
        ans = []
        helper(root,ans)
        return ans