class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        
        if sums %2 != 0:
            return False
        
        sums = int(sums/2)
        
        n = len(nums)
        
        dp = [[None for j in range(sums+1)]for i in range(n+1)]
        
        for j in range(sums+1):
            dp[0][j] = False
        
        for i in range(n+1):
            dp[i][0] = True
            
        for i in range(1,n+1):
            for j in range(1,sums+1):
                
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else :
                    dp[i][j] = dp[i-1][j]
                    
        return dp[n][sums]