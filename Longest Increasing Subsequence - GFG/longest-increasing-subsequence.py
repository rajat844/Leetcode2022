#User function Template for python3

class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
        # def helper(curr,prev):
        #     if curr == n:
        #         return 0
        #     ans = 0
        #     if prev == -1 or a[curr] > a[prev]:
        #         ans =  max(helper(curr+1,prev),1+helper(curr+1,curr))
        #     else :
        #         ans = helper(curr+1,prev)
            
        #     return ans
        
        # return helper(0,-1)
        
        # dp = [[0 for i in range(n+1)] for j in range(n + 1)]
        
        # for ind in range(n-1,-1,-1):
        #     for prev_ind in range(ind-1,-2,-1):
                
        #         if prev_ind == -1 or  a[ind] > a[prev_ind]:
        #             dp[ind][prev_ind + 1] = max(dp[ind + 1][prev_ind + 1], 1+ dp[ind +1 ][ind + 1])
        #         else :
        #             dp[ind][prev_ind + 1] = dp[ind+1][prev_ind+1]
                
        
        # return dp[0][0]
        
        dp = [1 for i in range(n)]
        
        for i in range(n):
            for j in range(i-1,-1,-1):
                if a[i] > a[j]:
                    dp[i] = max(1+dp[j],dp[i])
                    
        return max(dp)
        
    
        
                
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends