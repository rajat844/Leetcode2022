class Solution:
    def nthUglyNumber(self, n: int) -> int:
        a = 0
        b = 0
        c = 0
        dp = [None for i in range(n)]
        dp[0] = 1
        
        for i in range(1,n):
            x = 2*dp[a]
            y = 3*dp[b]
            z = 5*dp[c]
            
            dp[i] = min(x,y,z)
            if dp[i] == x: a += 1
            if dp[i] == y: b += 1
            if dp[i] == z: c += 1
        
        return dp[-1]