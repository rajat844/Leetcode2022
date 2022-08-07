class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [1] * 5
        for i in range(1,n):
            a,e,i,o,u = dp
            dp[0] = e+i+u
            dp[1] = a+i
            dp[2] = e+o
            dp[3] = i
            dp[4] = i+o
        
        return sum(dp) % (10**9 + 7)