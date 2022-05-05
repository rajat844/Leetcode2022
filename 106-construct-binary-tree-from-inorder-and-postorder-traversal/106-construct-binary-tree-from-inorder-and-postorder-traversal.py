# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        st = {}
        for i in range(n):
            st[inorder[i]] = i
            
        def helper(instart,inend,poststart,postend):
            if poststart > postend or instart > inend:
                return None
            
            x = postorder[postend]
            
            node = TreeNode(x)
            
            in_idx = st[x]
            d = in_idx - instart
            
            node.left = helper(instart,in_idx - 1,poststart,poststart + d - 1)
            node.right = helper(in_idx + 1, inend,poststart+d,postend - 1)
            
            return node
        
        return helper(0,n-1,0,n-1)
        