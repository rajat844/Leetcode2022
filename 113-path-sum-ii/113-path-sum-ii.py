# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        def isleaf(node):
            if node.left == None and node.right == None:
                return True
            return False
        
        def helper(node,arr):
            nonlocal ans
            arr.append(node.val)
            
            if isleaf(node) is True:
                if sum(arr) == targetSum:
                    ans.append(arr[::])
            
            else:
                if node.left:
                    helper(node.left,arr)
                if node.right:
                    helper(node.right,arr)
            
            arr.pop()
        
        ans = []
        helper(root,[])
        return ans
        