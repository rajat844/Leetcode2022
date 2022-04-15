#User function Template for python3
from collections import deque
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        visited = [False for i in range(V)]
        def bfs(node):
            visited[node] = True
            st = deque()
            st.append(node)
            
            while len(st) > 0:
                currnode = st.popleft()
                ans.append(currnode)
                for x in adj[currnode]:
                    if visited[x] == False:
                        visited[x] = True
                        st.append(x)
            
        ans = []
        bfs(0)
        
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