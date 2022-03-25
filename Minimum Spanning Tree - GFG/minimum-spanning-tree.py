#User function Template for python3

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        def findParent(node):
            if parent[node] == node:
                return node
            parent[node] = findParent(parent[node])
            return parent[node]
        
        def union(node1 , node2):
            node1 = findParent(node1)
            node2 = findParent(node2)
            
            if rank[node1] == rank[node2]:
                rank[node2] += 1
                parent[node2] = node1
            
            if rank[node1] > rank[node2]:
                parent[node1] = node2
                
            if rank[node2] > rank[node1]:
                parent[node2] = node1
                
            
        #code here
        parent = []
        rank = []
        
        for i in range(V):
            parent.append(i)
            rank.append(0)
        
        st = []
        
        for i in range(len(adj)):
            for j in adj[i]:
              st.append((i,j[0],j[1]))
              
        st.sort(key = lambda x: x[2])
        
        ans = 0
        mst = []
        for i in range(len(st)):
            node1,node2,edge = st[i]
            if findParent(node1) != findParent(node2):
                union(node1,node2)
                ans += edge
                mst.append((node1,node2))
                
        return ans

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