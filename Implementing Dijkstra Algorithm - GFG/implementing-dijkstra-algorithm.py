import heapq,math
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        ans = [math.inf for i in range(V)]
        ans[S] = 0
        st = []
        st.append((0,S))
        heapq.heapify(st)
        
        while len(st) > 0:
            dist,node = heapq.heappop(st)
            for x in adj[node]:
                currnode = x[0]
                currdist = x[1]
                
                if ans[currnode] > currdist + dist:
                    ans[currnode] = currdist + dist
                    heapq.heappush(st,(currdist + dist,currnode))
                    
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