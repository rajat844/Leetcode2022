# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        st = deque([root])
        ans = []
        while len(st) > 0:
            x = len(st)
            temp = []
            while x :
                x -= 1
                node = st.popleft()
                temp.append(node.val)
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
            ans.append(temp)
        
        return ans[::-1]
            
            
            
        