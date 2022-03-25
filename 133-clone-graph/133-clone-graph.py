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
        
        def helper(node):
            if node in st:
                return st[node]
            
            cloneNode = Node(node.val)
            st[node] = cloneNode
            for x in node.neighbors:
                cloneNode.neighbors.append(helper(x))
            return cloneNode
        
        return helper(node)
            
        