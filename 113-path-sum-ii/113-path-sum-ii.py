# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def isRoot(node):
            if node.left == None and node.right == None:
                return True
            
            return False
        
        if root is None:
            return []
        
        def helper(node,s):
            
            nonlocal ans
            s.append(node.val)
            if isRoot(node) and sum(s) == targetSum:
                ans.append(s[::])
            
            if node.left:
                helper(node.left,s)
            if node.right:
                helper(node.right,s)
            s.pop()
            
        ans = [] 
        
        helper(root,[])
        return ans
            
        