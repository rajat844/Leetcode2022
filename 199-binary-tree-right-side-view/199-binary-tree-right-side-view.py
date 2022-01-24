# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        level = collections.deque()
        nodes = collections.deque()
        maxLevel = -1
        
        nodes.append(root)
        level.append(0)
        
        while len(nodes) > 0:
            currNode = nodes.popleft()
            currLevel = level.popleft()
            
            if currNode and currLevel > maxLevel:
                maxLevel = currLevel
                ans.append(currNode.val)
                
            if currNode :
                if currNode.right:
                    nodes.append(currNode.right)
                    level.append(currLevel + 1)
                if currNode.left:
                    nodes.append(currNode.left)
                    level.append(currLevel + 1)
        return ans
        
                    
        