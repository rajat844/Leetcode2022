import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf for i in range(amount+1)]
        dp[0] = 0

        for i in range(1, amount+1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    if dp[i-coins[j]] != math.inf and dp[i-coins[j]] + 1 < dp[i]:
                        dp[i] = dp[i-coins[j]] + 1

        if  dp[amount] == math.inf:
            return -1
        
        return int(dp[amount])
