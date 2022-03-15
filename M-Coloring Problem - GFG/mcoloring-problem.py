#User function Template for python3
from collections import defaultdict
#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, m, N):
    color = [0 for i in range(N)]
    
    def allowed(node,col):
        for k in range(N):
            if k != node and graph[k][node] == 1 and color[k] == col:
                return False
        return True
    
    def helper(node):
        if node == N:
            return True
        
        for i in range(1,m+1):
            if allowed(node,i):
                color[node] = i
                if helper(node+1):
                    return True
                color[node] = 0
        
        return False
        
    return helper(0)
    
    #your code here
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends