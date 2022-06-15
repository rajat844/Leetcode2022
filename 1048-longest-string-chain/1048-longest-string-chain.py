class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        ans = 1
        
        words.sort(key = len)
        
        for w in words:
            dp[w] = 1
            for i in range(len(w)):
                prev = w[:i] + w[i+1:]
                
                if prev in dp:
                    dp[w] = max(dp[w],1+dp[prev])
                    ans = max(dp[w],ans)
        
        return ans