#User function Template for python3
from collections import deque
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        visited = [False for i in range(V)]
        ans = []
        q = deque()
        q.append(0)
        visited[0] = True
        
        while len(q) > 0:
            node = q.popleft()
            ans.append(node)
            
            for x in adj[node]:
                if visited[x] == False:
                    visited[x] = True
                    q.append(x)
        
        return ans

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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends