class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(arr):
            n = len(arr)
            
            dp = [-1 for i in range(n+2)]
            
            dp[n] = dp[n+1] = 0
            
            for i in range(n-1,-1,-1):
                dp[i] = max(arr[i] + dp[i+2] ,dp[i+1])
            
            return dp[0]
        
        return max(helper(nums[1:]),helper(nums[:len(nums)-1]))
        
            
            
            
            
        