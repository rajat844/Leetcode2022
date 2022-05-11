class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for i in range(len(nums))]
        
        def helper(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            
            case1 = nums[i] + helper(i+2)
            case2 = helper(i+1)
            
            dp[i] = max(case1,case2)
            
            return dp[i]
        
        return helper(0)
            
            