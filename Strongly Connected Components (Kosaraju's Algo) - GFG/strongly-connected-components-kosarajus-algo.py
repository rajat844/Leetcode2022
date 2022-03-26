#User function Template for python3

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        visited  = [False for i in range(V)]
        toposort = []
        def dfs(node):
            visited[node] = True
            
            for x in adj[node]:
                if visited[x] == False:
                    dfs(x)
                    
            toposort.append(node)
        
        for i in range(V):
            if visited[i] == False:
                dfs(i)
                
        transpose = [[] for i in range(V)]
        
        for i in range(V):
            visited[i] = False
            for x in adj[i]:
                transpose[x].append(i)
                
        cnt = 0
        
        def rdfs(node):
            visited[node] = True
            for x in transpose[node]:
                if visited[x] == False:
                    rdfs(x)
            
        while len(toposort) > 0:
            node = toposort.pop()
            if visited[node] == False:
                cnt += 1
                rdfs(node)
        
        return cnt
        
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends