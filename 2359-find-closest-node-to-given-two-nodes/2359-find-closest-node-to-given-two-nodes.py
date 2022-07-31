class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(node,dist):
            st = deque()
            st.append((node,0))
            
            while len(st) > 0:
                i,d = st.popleft()
                dist[i] = d
                if edges[i] != - 1 and dist[edges[i]] == math.inf:
                    st.append((edges[i],d+1))
        
        dist1 = [math.inf for i in range(len(edges))]
        dist2 = [math.inf for i in range(len(edges))]
        bfs(node1,dist1)
        bfs(node2,dist2)
        
        s = math.inf
        ans = -1
        for i in range(len(edges)):
            x = max(dist1[i],dist2[i])
            if s > x:
                ans = i
                s = x
        return ans

                
                