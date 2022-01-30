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
        
        def helper(prestart,preend,instart,inend):
            if prestart > preend or instart > inend:
                return None
            
            root = TreeNode(preorder[prestart])
            
            inroot = dict[root.val]
            numsleft = inroot-instart
            
            root.left = helper(prestart+1,prestart+numsleft,instart,inroot-1)
            root.right = helper(prestart+numsleft+1,preend,inroot+1,inend)
            return root
            
        root = helper(0,len(preorder)-1,0,len(inorder)-1)
        return root