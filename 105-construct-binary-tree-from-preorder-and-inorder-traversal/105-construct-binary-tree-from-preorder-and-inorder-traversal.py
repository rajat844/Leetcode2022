# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dict = {}
        for i in range(len(inorder)):
            dict[inorder[i]] = i
            
        def helper(instart,inend,prestart,preend):
            if instart > inend or prestart > preend:
                return None
            
            root = TreeNode(preorder[prestart])
            
            inroot = dict[root.val]
            numleft = inroot-instart
            
            root.left = helper(instart,inroot-1,prestart+1,prestart+numleft)
            root.right = helper(inroot+1,inend,prestart+numleft+1,preend)
            return root
        
        root = helper(0,len(inorder) - 1,0,len(preorder)-1)
        return root
            