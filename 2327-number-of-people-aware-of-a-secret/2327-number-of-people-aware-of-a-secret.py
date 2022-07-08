class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0 for i in range(n)]
        dp[0] = 1
        prev = 0
        
        for i in range(1,n):
            fr_ppl = 0 if (i - forget < 0 or dp[i-forget] < 0) else dp[i-forget]
            dl_ppl = 0 if (i - delay < 0 or dp[i-delay] < 0) else dp[i-delay]
            
            dp[i] = prev + dl_ppl - fr_ppl
            prev = dp[i]
        
        ans = 0
        for i in range(forget):
            ans += dp[n-i-1]
        
        return ans % (10**9 + 7)