class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0 for i in range(n)]
        dp[0] = 1
        for i in range(1,n):
            for j in range(i-forget+1, i-delay+1):
                if i < 0:
                    continue
                dp[i] += dp[j]
        
        return sum(dp[-forget:]) % (10**9+7)  