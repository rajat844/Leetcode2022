from collections import deque
class Solution:
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
		#Code here
		visited = [False for i in range(V)]
		
		def helper(node):
		    visited[node] = True
		    st = deque()
		    st.append((node,-1))
		    
		    while len(st) > 0:
		        currnode,parent = st.popleft()
		        
		        for x in adj[currnode]:
		            if visited[x] == False:
		                st.append((x,currnode))
		                visited[x] = True
		            elif parent != x:
		                return True
		    return False
		
		
		for i in range(V):
		    if visited[i] == False:
		        if helper(i) == True:
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