# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import defaultdict, deque
    
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        storage = defaultdict(lambda:defaultdict(list))
        items = deque()

        items.append((root, 0, 0))

        while len(items) > 0:
            currNode, currX, currY = items.popleft()
            storage[currX][currY].append(currNode.val)

            if currNode.left:
                items.append((currNode.left, currX-1, currY+1))
            if currNode.right:
                items.append((currNode.right, currX+1, currY+1))
        ans = []
        for i in sorted(storage):
            temp = []
            for j in sorted(storage[i]):
                for k in sorted(storage[i][j]):
                    temp.append(k)
            ans.append(temp)
        
        return ans