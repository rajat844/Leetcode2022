import math
from collections import deque
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        dist = [math.inf] * V
        q = deque()
        dist[S] = 0
        q.append(S)
        while len(q) > 0:
            node = q.popleft()
            d = dist[node]
            
            if d != math.inf:
                for x in adj[node]:
                    if dist[x[0]] > d + x[1]:
                        dist[x[0]] = min(dist[x[0]],d+x[1])
                        q.append(x[0])
                    
        return dist
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends