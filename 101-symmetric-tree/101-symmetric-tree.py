# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def preordercomp(leftroot,rightroot):
            try:
                if leftroot is None and rightroot is None:
                    return True
                else :
                    return leftroot.val == rightroot.val and preordercomp(leftroot.left,rightroot.right) and preordercomp(leftroot.right,rightroot.left)
            
            except:
                return False
                        
        return preordercomp(root.left,root.right)
        