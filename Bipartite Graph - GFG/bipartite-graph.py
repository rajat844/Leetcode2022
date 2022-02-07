from collections import deque
class Solution:
	def isBipartite(self, V, adj):
		#code here
		def dfs(node,color):
		    vis[node] = color
		    
		    for x in adj[node]:
		        if vis[x] == -1:
		            if color == 0:
		                if dfs(x,1) == False:
		                    return False
		            else :
		                if dfs(x,0) == False:
		                    return False
		        elif(vis[x] == color) :
		            return False
		    return True
		
		vis = [-1]*V
		for i in range(V):
		    if vis[i] == -1:
		        if dfs(i,0) == False:
		            return False
		
		return True
		
		        

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends