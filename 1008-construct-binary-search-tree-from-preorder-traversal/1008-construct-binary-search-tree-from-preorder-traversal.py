# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:   
        def helper(upperbound):
            nonlocal i
            if i == len(preorder) or preorder[i] > upperbound:
                return None
           
            x = preorder[i]
            node = TreeNode(x)
            i += 1
            node.left = helper(x)
            node.right = helper(upperbound)
            
            return node
        i = 0
        return helper(1001)
            
            

        