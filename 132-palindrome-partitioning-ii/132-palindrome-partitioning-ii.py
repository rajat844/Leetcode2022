class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [None for i in range(n+1)]
        dp[n] = 0
        
        for i in range(n-1,-1,-1):
            ans = math.inf
            for x in range(i,n):
                if s[i:x+1] == s[i:x+1][::-1]:
                    ans = min(ans,1+dp[x+1])
            dp[i] = ans
        
        return dp[0] - 1
    
#         def recursion(i):
#             if i == n:
#                 return 0
#             ans = math.inf
#             for x in range(i,n):
#                 if s[i:x+1] == s[i:x+1][::-1]:
#                     ans = min(1+recursion(x+1),ans)
#             return ans
        
#         n = len(s)
#         return recursion(0) - 1
    
            
        