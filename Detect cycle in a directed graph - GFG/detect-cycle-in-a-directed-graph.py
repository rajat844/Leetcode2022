#User function Template for python3
from collections import deque
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        st = [0]*V
        for i in range(V):
            for x in adj[i]:
                st[x] += 1
        
        q = deque()
               
        for i in range(len(st)):
            if st[i] == 0:
                q.append(i)
        c = 0        
        while len(q) > 0:
            node = q.popleft()
            c += 1
            for x in adj[node]:
                st[x] -= 1
                if st[x] == 0:
                    q.append(x)
                elif st[x] < 0:
                    return True
                    break
                
        if c == V:
            return False      
        return True

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends