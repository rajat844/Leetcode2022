# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        st = deque()
        st.append(root)
        ans = []
        
        while len(st) > 0:
            k,p = len(st),len(st)
            s = 0
            while k > 0:
                k -= 1
                node = st.popleft()
                s += node.val
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
            ans.append(s/p)
            p = 0
        return ans