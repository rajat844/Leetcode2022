# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
            
        def helper(instart,inend,poststart,postend):
            if poststart > postend or instart > inend:
                return None
            
            root = TreeNode(postorder[postend])
            
            inroot = dic[root.val]
            rootleft = inroot-instart
            
            root.left = helper(instart,inroot-1,poststart,poststart+rootleft-1)
            root.right = helper(inroot+1,inend,poststart+rootleft,postend-1)
            return root
        
        root = helper(0,len(inorder) -1,0,len(postorder) -1)
        return root
        