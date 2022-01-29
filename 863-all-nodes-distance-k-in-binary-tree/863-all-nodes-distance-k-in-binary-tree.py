# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def getParents(self, node: TreeNode,parent :TreeNode)->None:
        if node is None:
            return 
        
        self.parent[node.val] = parent
        self.getParents(node.left,node)
        self.getParents(node.right,node)
        
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.parent = {}
        self.getParents(root,None)
        return self.bfs(target,k)
    
    def bfs(self, target: TreeNode , k: int)->List[int]:
        res, q, visited = [], [(target,0)] ,set()
        while q:
            n,d = q.pop(0)
            if n not in visited:
                if d==k :
                    res.append(n.val)
                visited.add(n)
                
                if n.left:
                    q.append((n.left,d+1))
                if n.right :
                    q.append((n.right,d+1))
                if self.parent[n.val]: 
                    q.append((self.parent[n.val],d+1))
        return res
                    