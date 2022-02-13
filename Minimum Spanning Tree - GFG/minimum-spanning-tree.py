#User function Template for python3
import math
from queue import PriorityQueue
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        keyArr = [math.inf]*V
        parentArr = [-1]*V
        isMST = [False]*V
        
        keyArr[0] = 0
        
        q = PriorityQueue()
        q.put((0,0))
        
        while not q.empty() :
            currKey, node = q.get()
            isMST[node] = True
            
            for x in adj[node]:
                childnode = x[0]
                childkey = x[1]
                
                if isMST[childnode] == False and keyArr[childnode] > childkey:
                    keyArr[childnode] = childkey
                    q.put((childkey,childnode))
                    parentArr[childnode] = node
        
        return sum(keyArr)
        
        
                
                
        
        
        

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