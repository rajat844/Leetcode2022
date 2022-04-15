#User function Template for python3
class Solution:
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        visited = [False for i in range(V)]
        currvisited = [False for i in range(V)]
        
        def dfs(node):
            visited[node] = True
            currvisited[node] = True
            
            for x in adj[node]:
                if visited[x] == False:
                    if dfs(x) == True:
                        return True
                elif currvisited[x] == True:
                    return True
            
            currvisited[node] = False
            return False
        
        for i in range(V):
            if visited[i] == False:
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