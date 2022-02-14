#User function Template for python3
class Solution:
    def spanningTree(self, V, adj):
        # sorting the adj nodes according to cost/ weight 
        Adj = []
        for node in range(V):
            for dest, cost in adj[node]:
                Adj.append([node, dest, cost])
        Adj.sort(key = lambda x : x[2])  
        
        # creating parent and rank arr
        parent_arr = []
        rank_arr = [0]*V
        for node in range(V):
            parent_arr.append(node)
            
        # Disjoint set data structure 
        def findParent(node):
            if node == parent_arr[node]:
                return node
            parent_arr[node] = findParent(parent_arr[node])
            return parent_arr[node]
            
        def union(node1, node2):
            node1 = findParent(node1)
            node2 = findParent(node2)
            
            if rank_arr[node1] < rank_arr[node2]:
                parent_arr[node1] = node2
            elif rank_arr[node1] > rank_arr[node2]:
                parent_arr[node2] = node1
            else:
                parent_arr[node2] = node1
                rank_arr[node1]+=1
        

        min_cost = 0
        res_tree = [] # this is optional this will store the tree itself
    
        for arr in Adj:
            src = arr[0]
            dest = arr[1]
            cost = arr[2]
            if findParent(src)!=findParent(dest):
                min_cost += cost
                res_tree.append((src, dest))
                union(src, dest)
        return min_cost
            
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