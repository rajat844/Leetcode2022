# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        curr  = root
        
        while (curr):
            if curr.left is None:
                inorder.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right != curr and prev.right != None:
                    prev = prev.right
                
                if prev.right == None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    inorder.append(curr.val)
                    curr = curr.right
        return inorder