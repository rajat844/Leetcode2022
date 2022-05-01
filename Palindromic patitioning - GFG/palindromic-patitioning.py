#User function Template for python3
import math
class Solution:
    def palindromicPartition(self, string):
        def isPalindrome(start,end):
            while start < end:
                if string[start] != string[end]:
                    return False
                start += 1
                end -= 1
            return True
        # code here
        def helper(i,j):
            if dp[i][j] != -1:
                return dp[i][j]
            if i > j:
                dp[i][j] = 0
                return dp[i][j]
            
            elif isPalindrome(i,j):
                dp[i][j] = 0
                return dp[i][j]
                
            else :
                dp[i][j] = math.inf
                for k in range(i,j):
                    if isPalindrome(i,k) == False:
                        continue
                    ans1 = dp[i][k] if dp[i][k] != -1 else helper(i,k)
                    ans2 = dp[k+1][j] if dp[k+1][j] != -1 else helper(k+1,j)
                    
                    dp[i][j] = min(ans1+ans2+1,dp[i][j])
                
                return dp[i][j]
        
        n = len(string)
        dp = [[-1 for i in range(n+1)]for i in range(n+1)]
        return helper(0,len(string) - 1)
        

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