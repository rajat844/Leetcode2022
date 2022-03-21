# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
            
        def helper(prestart,preend,instart,inend):
            if prestart > preend or instart > inend:
                return None
            
            node = TreeNode(preorder[prestart])
            
            x = dic[node.val]
            num_ele = x - instart
            
            node.left = helper(prestart+1, prestart + x, instart,x-1)
            node.right = helper(prestart+num_ele+1,preend,x+1,inend)
            return node
        
        root = helper(0,len(preorder) - 1,0,len(inorder) - 1)
        return root
        