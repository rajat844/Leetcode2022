#User function Template for python3
from collections import deque
class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        st = deque()
        for i in range(n):
            st.append(i)
        
        while len(st) >= 2:
            a = st.pop()
            b = st.pop()
            
            if M[a][b] == 1:
                st.append(b)
            else :
                st.append(a)
                
        
        x = st.pop()
        
        for i in range(n):
            if M[x][i] == 1:
                return -1
        
        for i in range(n):
            if i!= x:
                if M[i][x] == 0:
                    return -1
        return x
                
                
            
                
            


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends