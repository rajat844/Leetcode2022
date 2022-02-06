from collections import deque
class Solution:
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
		#Code here
		def detectCycle(i):
		    vis[i-1] = True 
		    st = deque()
		    st.append((i,-1))
		    
		    while len(st) > 0:
		        node,parent = st.popleft()
		        
		        for x in adj[node]:
		            if vis[x - 1] is True :
		                if x != parent:
		                    return True
		            else:
		                vis[x-1] = True
		                st.append((x,node))
		    return False 
		    
		vis = [False] * V
		
		for i in range(1,V):
		    if vis[i-1] == False:
		        if detectCycle(i) : return True
		    
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