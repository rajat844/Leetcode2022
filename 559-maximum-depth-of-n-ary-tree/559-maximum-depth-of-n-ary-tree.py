"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        st = deque()
        st.append(root)
        height = 0
        
        while len(st) > 0:
            k = len(st)
            while k > 0:
                k -= 1
                node = st.popleft()
                if node.children != None:
                    st.extend(node.children)
            
            height += 1
        
        return height
        
        