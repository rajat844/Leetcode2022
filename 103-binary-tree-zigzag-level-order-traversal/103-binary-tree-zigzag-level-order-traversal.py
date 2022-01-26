# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        st = collections.deque()
        ans = []
        lefttoright = True
        
        st.append(root)
        
        while len(st) > 0:
            currAns = []
            currSt = collections.deque()
            
            while len(st) > 0:
                currSt.append(st.popleft())
                
            if lefttoright is True:
                while len(currSt) > 0 :
                    node = currSt.popleft()
                    if node :
                        currAns.append(node.val)
                        st.append(node.left)
                        st.append(node.right)
            if lefttoright is False:
                while len(currSt) > 0 :
                    node = currSt.popleft()
                    if node:
                        currAns.append(node.val)
                        st.append(node.right)
                        st.append(node.left)                
            
            if len(currAns) is not 0:
                ans.append(currAns)
                
            lefttoright = not lefttoright
            st.reverse()
            
        return ans
        