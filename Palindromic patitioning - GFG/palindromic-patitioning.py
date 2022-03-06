#User function Template for python3
import sys
class Solution:
    def palindromicPartition(self, string):
        # code here
        n = len(string)
        dp = [[-1 for j in range(n+1)]for i in range(n+1)]
        
        def isPalidrome(start,end):
            while start < end:
                if string[start] != string[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def solve(i,j):
            if dp[i][j] != -1:
                return dp[i][j]
                
            if i > j :
                dp[i][j] = 0
                return dp[i][j]
             
            if isPalidrome(i,j):
                dp[i][j] = 0
                return dp[i][j]
            
           
            ans = sys.maxsize
            
            for k in range(i,j):
                
                if isPalidrome(i,k) == False:
                    continue
                
                if dp[i][k] != -1:
                    temp1 = dp[i][k]
                else :
                    temp1 = solve(i,k)
                
                if dp[k+1][j] != -1:
                    temp2 = dp[k+1][j]
                else:
                    temp2 = solve(k+1,j)
                    
                ans = min(ans,temp1 + temp2 + 1)
                
            dp[i][j] = ans
            return dp[i][j]
                
                
                
            
        
        return solve(0,n-1)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends