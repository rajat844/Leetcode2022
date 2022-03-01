class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        arrSum = sum(nums)
        if target > arrSum:
            return 0
        t = (arrSum + target)/2
        
        if int(t) == t:
            t = abs(int(t))
        else:
            return 0
        
        def countSubsets():
            
            n = len(nums)
            dp = [[0 for j in range(t+1)]for i in range(n+1)]
            
            for i in range(n+1):
                dp[i][0] = 1
            
            for i in range(1,n+1):
                for j in range(0,t+1):
                    
                    if j >= nums[i-1]:
                        dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                        
                    else:
                        dp[i][j] = dp[i-1][j]
            
            return dp[n][t]
        
        return countSubsets()
        