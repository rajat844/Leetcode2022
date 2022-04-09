class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [-1 for i in range(n+1)]
        dp[0] = 0
        flag = 1
        
        for i in range(1,n+1):
            if i == 2*flag:
                flag = i
            dp[i] = 1 + dp[i-flag]
        
        return dp
                
        