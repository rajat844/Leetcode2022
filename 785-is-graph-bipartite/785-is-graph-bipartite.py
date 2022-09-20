class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bfs(node):
            st = deque()
            st.append((node,0))
            color[node] = 0
            
            while len(st) > 0:
                curr,c = st.popleft()
            
                
                for x in graph[curr]:
                    if color[x] == None:
                        st.append((x,1-c))
                        color[x] = 1-c
                    elif color[x] == c:
                        return False
                
            return True
        
        color = [None for i in range(len(graph))]
        
        for i in range(len(graph)):
            if color[i] == None:
                if bfs(i) == False:
                    return False
        
        return True
    
        