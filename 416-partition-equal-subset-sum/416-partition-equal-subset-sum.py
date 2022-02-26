class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numSum = sum(nums)
        if numSum % 2 == 1:
            return False
        else:
            numSum = numSum//2
            
        n = len(nums)
        
        dp = [[False] * (numSum+1)for j in range(n+1)]
            
        for i in range(n+1):
            for j in range(numSum+1):
                if j == 0:
                    dp[i][j] = True
                elif nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else :
                    dp[i][j] = dp[i-1][j]
                    
        return dp[n][numSum]
        