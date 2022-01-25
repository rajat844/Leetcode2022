# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        height = 0
        
        storage = collections.deque()
        storage.append([root,1])
        
        while len(storage) > 0:
            x = storage.pop()
            node = x[0]
            level = x[1]
            if node is not None:
                if level > height:
                    height = level
                storage.append([node.left,level+1])
                storage.append([node.right,level+1])
                
        return height
                