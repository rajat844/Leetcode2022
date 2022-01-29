# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        st = deque()
        st.append((root,0))
        ans = 0
        while len(st) > 0:
            y = []
            while len(st) > 0:
                y.append(st.popleft())
            
            first = mini = y[0][1]
            last = y[-1][1]
            
            for i in range(len(y)):
                node,level = y[i]
                pr = level-mini + 1
                
                if node.left:
                    st.append((node.left,2*pr+1))
                if node.right:
                    st.append((node.right,2*pr+2))
                    
            ans = max(ans,last-first+1)
        
        return ans
                
        