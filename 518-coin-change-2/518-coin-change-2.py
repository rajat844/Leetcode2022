class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1 for j in range(amount+1)]for i in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = 1
        
        for j in range(amount+1):
            dp[0][j] = 0
        
        for i in range(1,n+1):
            for j in range(1,amount+1):
                if j >= coins[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[n][amount]