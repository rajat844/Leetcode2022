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
        
        def dfs(node,visited):
            if node in visited:
                return visited[node]
            
            newnode = Node(node.val)
            visited[node] = newnode
            
            if node.neighbors:
                for x in node.neighbors:
                    newnode.neighbors.append(dfs(x,visited))
            
            return newnode
        
        return dfs(node,{})
                    
            
                    
        