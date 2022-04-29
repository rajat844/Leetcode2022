# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        
        st = deque()
        st.append(root)
        
        while len(st) > 0:
            temp = []
            while len(st) > 0:
                temp.append(st.popleft())
            tempans = []
            for i in range(len(temp)):
                node = temp[i] 
                tempans.append(node.val)
                
                if node.left:
                    st.append(node.left)
                
                if node.right:
                    st.append(node.right)
            
            ans.append(tempans)
            
        return ans