# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        curr =  root
        
        while (curr):
            
            if curr.left == None:
                preorder.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right != None and prev.right != curr:
                    prev = prev.right
                
                if prev.right == None:
                    preorder.append(curr.val)
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    curr = curr.right
        
        return preorder
                