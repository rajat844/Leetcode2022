#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        def helper(i,j,s):
            if 0 <= i < n and 0 <= j < n and m[i][j] == 1:
                m[i][j] = 0
                
                if i == n-1 and j == n-1:
                    m[i][j] = 1
                    ans.append(s[::])
                    return 
            
                helper(i+1,j,s+'D')
                helper(i-1,j,s+'U')
                helper(i,j+1,s+'R')
                helper(i,j-1,s+'L')
            
                m[i][j] = 1
        
        ans = []
        if m[0][0] == 1:
            helper(0,0,"")
        return ans
        
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends