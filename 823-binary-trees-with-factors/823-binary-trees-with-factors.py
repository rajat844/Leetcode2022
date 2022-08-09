class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = {}
        
        for i in range(len(arr)):
            dp[arr[i]] = 1
            
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    key = int(arr[i]/arr[j])
                    if key in dp:
                        dp[arr[i]] += dp[arr[j]] * dp[key]
            
        ans = 0
        for k in dp:
            ans += dp[k]
        return ans%(10**9 + 7)