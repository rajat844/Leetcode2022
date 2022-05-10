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
        
        def helper(head):
            if head in st:
                return st[head]
            if head:
                cl_head = Node(head.val)
                st[head] = cl_head
                
            if head.neighbors == None:
                cl_head.neighbors = None
            
            else:
                for x in head.neighbors:
                    cl_head.neighbors.append(helper(x))
                    
            return cl_head
        
        st = {}
        return helper(node)
                
            
        