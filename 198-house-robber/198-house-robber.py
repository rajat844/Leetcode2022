class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for i in range(len(nums)+2)]
        
        dp[len(nums)] = dp[len(nums)+1] = 0
        
        for i in range(len(nums)-1,-1,-1):
            dp[i] = max(nums[i] + dp[i+2],dp[i+1])
        
        return dp[0]
            

            