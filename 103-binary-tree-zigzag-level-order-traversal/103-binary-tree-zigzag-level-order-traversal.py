# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        st = deque()
        ans = []
        ltor = True
        
        st.append(root)
        
        while len(st) > 0 :
            smallans = []
            temp = deque()
            
            while len(st) > 0:
                temp.append(st.popleft())
                
            if ltor == True:
                while len(temp) > 0:
                    node = temp.popleft()
                    if node:
                        smallans.append(node.val)
                        st.append(node.left)
                        st.append(node.right)
            
            else:
                while len(temp) > 0:
                    node = temp.popleft()
                    if node:
                        smallans.append(node.val)
                        st.append(node.right)
                        st.append(node.left)
            
            ltor = not ltor
            st.reverse()
            if len(smallans) > 0:
                ans.append(smallans)
        
        return ans
                    
        