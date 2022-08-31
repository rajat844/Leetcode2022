class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        
        def burst(i,j):
            if dp[i][j] != -1:
                return dp[i][j]
            if i > j:
                dp[i][j] = 0
                return dp[i][j]
            
            ans = -math.inf
            for x in range(i,j+1):
                ans = max(nums[i-1]*nums[x]*nums[j+1] + burst(i,x-1) + burst(x+1,j),ans)
            
            dp[i][j] = ans
            return dp[i][j]
        
        dp = [[-1 for i in range(n+2)] for j in range(n+2)]
        return burst(1,n)
    
                
                
            
        