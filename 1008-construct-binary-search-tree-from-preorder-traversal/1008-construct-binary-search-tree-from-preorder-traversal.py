# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        inorder = sorted(preorder)
        st = {}
        
        for i in range(len(inorder)):
            st[inorder[i]] = i
        
        def helper(prestart,preend,instart,inend):
            if prestart > preend:
                return None
            x = preorder[prestart]
            node = TreeNode(x)
            
            inidx = st[x]
            d = inidx - instart
            
            node.left = helper(prestart + 1,prestart + d,instart,inidx - 1)
            node.right = helper(prestart + d + 1, preend,inidx + 1, inend)
            
            return node
        
        return helper(0,n-1,0,n-1)
        