import heapq,math
class Solution:
    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        ans = [math.inf for i in range(V)]
        st = [(0,S)]
        ans[S] = 0
        heapq.heapify(st)
        
        while len(st) > 0:
            distance,node = heapq.heappop(st)
            
            if distance != math.inf:
                for x in adj[node]:
                    if ans[x[0]] > distance + x[1]:
                        ans[x[0]] = distance + x[1]
                        heapq.heappush(st,(ans[x[0]],x[0]))
                        
        return ans
            
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