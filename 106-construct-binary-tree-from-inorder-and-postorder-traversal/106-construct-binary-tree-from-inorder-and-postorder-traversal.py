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
            
            node = TreeNode(postorder[postend])
            
            x = dic[postorder[postend]]
            num_ele = x-instart
            
            node.left = helper(instart,x-1,poststart,poststart+num_ele-1)
            node.right = helper(x+1,inend,poststart+num_ele,postend-1)
            
            return node
        root = helper(0,len(inorder)-1,0,len(postorder)-1)
        return root