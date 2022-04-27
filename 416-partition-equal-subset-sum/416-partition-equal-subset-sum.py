class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        s = s/2
        if s != int(s):
            return False
        
        s = int(s)
        
        dp = [[False for i in range(s+1)] for j in range(len(nums)+1)]
        
        for j in range(s+1):
            dp[0][j] = False
        
        for i in range(len(nums) + 1):
            dp[i][0] = True

        for i in range(1,len(nums) + 1):
            for j in range(1,s+1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else :
                    dp[i][j] = dp[i-1][j]
        
        return dp[len(nums)][s]
                    
        