class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [-1 for i in range(n+1)]
        val = 1
        dp[0] = 0
        
        for i in range(1,n+1):
            if 2 * val == i:
                val = i
            dp[i] =1 + dp[i-val]
            
        return dp