# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        st = deque()
        ans = 0
        st.append(root)
        
        while len(st) > 0:
            ans = 0
            k = len(st)
            while k > 0:
                k -= 1
                node = st.popleft()
                ans += node.val
                
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
        
        return ans
        
        