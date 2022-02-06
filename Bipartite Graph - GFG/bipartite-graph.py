from collections import deque
class Solution:
	def isBipartite(self, V, adj):
		#code here
		def bfs(node):
		    st = deque([(node,0)])
		    vis[node] = 0
		    
		    while len(st) > 0:
		        curr,color = st.popleft()
		        for x in adj[curr]:
		            if vis[x] == -1:
		                if color == 0:
		                    st.append((x,1))
		                    vis[x] = 1
		                if color == 1:
		                    st.append((x,0))
		                    vis[x] = 0
		            elif vis[x] == color:
		                return False
		                
		    return True
		
		vis = [-1]*V
		for i in range(V):
		    if vis[i] == -1:
		        if bfs(i) == False:
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