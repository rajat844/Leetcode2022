class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        n = len(pressedKeys)
        dp = [-1 for i in range(n+1)]
        
        dp[0] = 1
        
        for i in range(1,n+1):
            dp[i] = dp[i-1]
            
            if i > 1 and pressedKeys[i-1] == pressedKeys[i-2]:
                dp[i] += dp[i-2]
            else :
                continue
            
            if i > 2 and pressedKeys[i-1] == pressedKeys[i-3]:
                dp[i] += dp[i-3]
            else:
                continue
                
            if (pressedKeys[i-1] == "9" or pressedKeys[i-1] == "7"):
                if i > 3  and pressedKeys[i-1] == pressedKeys[i-4]:
                    dp[i] += dp[i-4]
                else:
                    continue
        
        return dp[n] % (10**9 + 7)
        