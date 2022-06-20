class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for i in range(len(nums))]
        
        dp[n-1] = True
        
        for i in range(n-2,-1,-1):
            x = nums[i]
            for j in range(1,x+1):
                if dp[i+j] == True:
                    dp[i] = True
                    break
        
        return dp[0]
        