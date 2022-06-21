from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [False for i in range(n)]
        colors = [-1 for i in range(n)]
        
        for i in range(n):
            if visited[i] == False:
                visited[i] = True
                st = deque()
                st.append((i,0))
                
                while len(st) > 0:
                    node,color = st.popleft()
                    colors[node] = color
                    
                    for x in graph[node]:
                        if visited[x] == False:
                            visited[x] = True
                            st.append((x,1-color))
                        elif colors[x] == color:
                            return False
        
        return True
                    
                    
                
        
        