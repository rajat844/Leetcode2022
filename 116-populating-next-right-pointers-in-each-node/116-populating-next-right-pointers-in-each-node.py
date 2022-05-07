"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        st = deque()
        st.append(root)
        
        while len(st) > 0:
            k = len(st)
            while k > 1:
                k -= 1
                node = st.popleft()
                node.next = st[0]
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
            
            node = st.popleft()
            node.next = None
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
        
        return root
        