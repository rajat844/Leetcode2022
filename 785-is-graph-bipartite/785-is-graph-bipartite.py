class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node,color):
            visited[node] = True
            colors[node] = color
            
            for x in graph[node]:
                if visited[x] == False:
                    if dfs(x,1-color) == False:
                        return False
                elif colors[x] == color:
                    return False
            return True
        
        n = len(graph)
        colors = [-1 for i in range(n)]
        visited = [False for i in range(n)]
        
        for i in range(n):
            if visited[i] == False:
                if dfs(i,0) == False:
                    return False
        
        return True
            
        