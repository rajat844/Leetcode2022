# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def helper(node,clone_node):
            nonlocal ans
            if node is None:
                return
            helper(node.left,clone_node.left)
            if node == target:
                ans = clone_node
            helper(node.right,clone_node.right)
        
        ans = None
        helper(original,cloned)
        return ans