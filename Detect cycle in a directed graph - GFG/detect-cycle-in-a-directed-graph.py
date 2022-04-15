#User function Template for python3
from collections import deque
class Solution:
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        ans = []
        arr = [0 for i in range(V)]
        for i in range(V):
            for x in adj[i]:
                arr[x] += 1
        st = deque()       
        for i in range(len(arr)):
            if arr[i] == 0:
                st.append(i)
                
        while len(st) > 0:
            node = st.popleft()
            ans.append(node)
            
            for x in adj[node]:
                arr[x] -= 1
                if arr[x] == 0:
                    st.append(x)
        
        ans.reverse()
        if len(ans) == V:
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