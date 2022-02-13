#User function Template for python3
import math
from queue import PriorityQueue
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        keyArr = [math.inf] * V
        parentArr = [-1] * V
        isMst = [False] * V
        
        q = PriorityQueue()
        
        keyArr[0] = 0
        q.put((0,0))
        
        while q.empty() == False:
            Val, node = q.get()
            isMst[node] = True
            
            for x in adj[node]:
                chNode = x[0]
                chKey = x[1]
                
                if isMst[chNode] == False and keyArr[chNode] > chKey:
                    keyArr[chNode] = chKey
                    parentArr[chNode] = node
                    q.put((chKey,chNode))
                    
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