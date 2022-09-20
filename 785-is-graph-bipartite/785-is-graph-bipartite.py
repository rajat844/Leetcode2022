class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node,c):
            color[node] = c
            
            for x in graph[node]:
                if color[x] == None:
                    if dfs(x,1-c) == False:
                        return False
                
                elif color[x] == c:
                    return False
            
            return True
        
        color = [None for i in range(len(graph))]
        for i in range(len(graph)):
            if color[i] == None:
                if dfs(i,0) == False:
                    return False
        
        return True
        