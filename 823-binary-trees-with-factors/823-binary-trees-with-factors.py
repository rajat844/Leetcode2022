class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp = {}
        arr.sort()
        
        ans = 0
        for i in range(len(arr)):
            dp[arr[i]] = 1
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    x = int(arr[i]/arr[j])
                    if x in dp:
                        dp[arr[i]] += dp[arr[j]] * dp[x]
            ans += dp[arr[i]]
        
        return ans%(10**9+7)