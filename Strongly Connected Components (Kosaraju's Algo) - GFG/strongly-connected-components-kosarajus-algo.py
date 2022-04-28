#User function Template for python3

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        #topological sort
        def dfs(node):
            visited[node] = True
            for x in adj[node]:
                if visited[x] == False:
                    dfs(x)
            revtopo.append(node)
    
        revtopo = []
        visited = [False for i in range(V)]
        for i in range(V):
            if visited[i] == False:
                dfs(i)
        
        #change the directions of nodes
        revadj = {}
        for i in range(V):
            revadj[i] = []
        
        for i in range(V):
            visited[i] = False
            for x in adj[i]:
                revadj[x].append(i)
                
        #do dfs now for the revadj 
        ans = 0
        def dfs2(node):
            visited[node] = True
            for x in revadj[node]:
                if visited[x] == False:
                    dfs2(x)
        
        while len(revtopo) > 0:
            i = revtopo.pop()
            if visited[i] == False:
                ans += 1
                dfs2(i)
                
        return ans
                
        
        
        
        
            
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