# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def isLeaf(root):
            if root.left == None and root.right == None:
                return True
            return False
        
        if root is None:
            return 0
        
        st = deque()
        height = 1
        st.append(root)
        
        while len(st) > 0:
            k = len(st)
            while k > 0:
                k -= 1
                node = st.popleft()
                if isLeaf(node) == True:
                    return height
                
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
            height += 1
        
        return height