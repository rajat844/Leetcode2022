# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import math
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def helper(upperbound):
            nonlocal i
            if i == len(preorder) or preorder[i] > upperbound:
                return None
            root = TreeNode(preorder[i])
            i += 1
            root.left = helper(root.val)
            root.right = helper(upperbound)
            return root
        
        i = 0
        return helper(math.inf)
            