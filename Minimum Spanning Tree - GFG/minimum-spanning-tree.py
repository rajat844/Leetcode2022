#User function Template for python3
import heapq,math
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        isMST = [False for i in range(V)]
        key = [math.inf for i in range(V)]
        st = []
        st.append((0,0))
        heapq.heapify(st)
        
        
        key[0] = 0
        
        while len(st) > 0:
            dist,node = heapq.heappop(st)
            isMST[node] = True
            
            for x in adj[node]:
                if isMST[x[0]] == False and key[x[0]] > x[1]:
                    key[x[0]] = x[1]
                    heapq.heappush(st,(x[1],x[0]))
                    
        return sum(key)
                
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends