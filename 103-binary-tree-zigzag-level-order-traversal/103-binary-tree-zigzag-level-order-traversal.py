# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return 
        
        st = deque()
        st.append(root)
        ltor = True
        ans = []
        while len(st) > 0:
            temp = deque()
            while len(st) > 0:
                temp.append(st.popleft())
            minans = []
            if ltor == True:
                while len(temp) > 0:
                    node = temp.popleft()
                    if node is not None:
                        minans.append(node.val)
                        st.append(node.left)
                        st.append(node.right)
            else:
                while len(temp) > 0:
                    node = temp.popleft()
                    if node is not None:
                        minans.append(node.val)
                        st.append(node.right)
                        st.append(node.left)
            
            if len(minans) > 0:
                ans.append(minans)
            st.reverse()
            ltor = not ltor
        
        return ans
                