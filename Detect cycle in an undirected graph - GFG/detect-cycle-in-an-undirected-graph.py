class Solution:
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
		#Code here
		visited = [False for i in range(V)]
		def helper(node,parent):
		    visited[node] = True
		    
		    for x in adj[node]:
		        if visited[x] == False:
		            if helper(x,node) == True:
		                return True
		        elif x != parent:
		            return True
		    return False
	        	
		for i in range(V):
		    if visited[i] == False:
		        if helper(i,-1) == True:
		            return True
		 
		return False

#{ 
#  Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends