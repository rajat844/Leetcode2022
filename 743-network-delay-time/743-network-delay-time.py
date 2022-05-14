import math
from collections import defaultdict,deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        
        for i in range(len(times)):
            adj[times[i][0]].append((times[i][1],times[i][2]))
            
        dist = [math.inf for i in range(n)]
        dist[k-1] = 0
        st = deque()
        st.append((k,0))
        
        while len(st) > 0:
            node,node_dist = st.popleft()
            
            if node in adj:
                for x in adj[node]:
                    currnode = x[0]
                    currdist = x[1]
                
                    if dist[currnode - 1] > currdist+node_dist:
                        dist[currnode-1] = currdist+node_dist
                        st.append((currnode,dist[currnode-1]))
        
        if math.inf not in dist:
            return max(dist)
        return  - 1
                                  
        
                        