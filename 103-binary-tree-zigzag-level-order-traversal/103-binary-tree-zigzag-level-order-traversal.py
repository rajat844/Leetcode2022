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
            return []
        st = deque()
        ltor = True
        
        ans = []
        st.append(root)
        
        while len(st) > 0:
            temp = []
            k = len(st)
            if ltor == True:
                while k > 0:
                    k -= 1
                    node = st.popleft()
                    temp.append(node.val)
                    if node.left:
                        st.append(node.left)
                    if node.right:
                        st.append(node.right)
            else :           
                while k > 0:
                    k -= 1
                    node = st.popleft()
                    temp.append(node.val)
                    if node.right:
                        st.append(node.right)
                    if node.left:
                        st.append(node.left)
            st.reverse()   
            if len(temp) > 0:
                ans.append(temp)
            ltor = not ltor
        
        return ans
            