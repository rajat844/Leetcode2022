#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        def dfs(node):
            vis[node] = True
            dfsvis[node] = True
            
            for x in adj[node]:
                if vis[x] == False:
                    if dfs(x) == True:
                        return True
                elif  dfsvis[x] == True:
                    return True
            
            dfsvis[node] = False
            return False
        
        
        vis = [False] * V
        dfsvis = [False] *V
        
        for i in range(V):
            if vis[i] == False:
                if dfs(i) == True:
                    return True
        return False

#{ 
#  Driver Code Starts
#Initial Template for Python 3

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
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends