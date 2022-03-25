"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        st = {}
        
        def helper(root):
            if root in st:
                return st[root]
            
            cloneroot = Node(root.val)
            st[root] = cloneroot
            for x in root.neighbors:
                cloneroot.neighbors.append(helper(x))
            
            return cloneroot
        
        return helper(node)