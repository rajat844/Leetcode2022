# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque()
        ans = []
        q.append(root)
 
        while len(q) > 0:
            st = []
            while len(q) > 0:
                st.append(q.popleft())
            currans = []
            for i in range(len(st)):
                node = st[i]
                currans.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            ans.append(currans)
        
        return ans
            
        