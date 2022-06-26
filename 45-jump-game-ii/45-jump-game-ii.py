import math
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for i in range(n)]
        dp[n-1] = 0
        
        for i in range(n-2,-1,-1):
            x = nums[i]
            ans = math.inf
            for j in range(i+1,i+x+1):
                if j >= n:
                    continue
                ans = min(ans,dp[j]+1)
            dp[i] = ans
        
        return dp[0]
                
        