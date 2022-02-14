#User function Template for python3

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        def findParent(node):
            if node == parent[node]:
                return node
            parent[node] = findParent(parent[node])
            return parent[node]
            
        def union(node1, node2):
            node1 = findParent(node1) 
            node2 = findParent(node2)
            if rank[node1] == rank[node2]:
                rank[node1] += 1
                parent[node1] = node2
            elif rank[node2] > rank[node1]:
                parent[node1] = node2
            elif rank[node1] > rank[node2]:
                parent[node2] = node1
                
    
        parent = []
        for node in range(V):
            parent.append(node)
        rank = [0] * V
        st = []
        for i in range(len(adj)):
            for j in adj[i]:
                st.append((j[1],j[0],i))
        
        st.sort(key = lambda x:x[0])
        ans = 0
        resTree = []
        for arr in st:
            edge, node1, node2 = arr[0],arr[1],arr[2]
            if findParent(node1) != findParent(node2) :
                union(node1,node2)
                resTree.append((node1,node2))
                ans += edge
        
        return ans
            
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends