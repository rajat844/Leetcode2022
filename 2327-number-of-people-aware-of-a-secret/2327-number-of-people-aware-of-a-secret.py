from collections import deque
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [None for i in range(n)]
        dp[0] = 1
        prev = 0
        
        for i in range(1,n):
            x = dp[i-forget] if i - forget >= 0 else 0
            y = dp[i-delay] if i -delay >= 0 else 0
            x = max(x,0)
            y = max(y,0)
            
            dp[i] = prev + y - x
            prev = dp[i]
        
        s = 0
        for i in range(forget):
            s += dp[n-i-1]
        
        return s % (10**9+7)