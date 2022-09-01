# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def recursion(node,mx):
            nonlocal ans
            if node is None:
                return 
            if node.val >= mx:
                mx = max(node.val,mx)
                ans += 1
            recursion(node.left,mx)
            recursion(node.right,mx)
            
        ans = 0
        recursion(root,-math.inf)
        return ans
            
        