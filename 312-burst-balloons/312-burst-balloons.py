class Solution:
    def maxCoins(self, nums: List[int]) -> int:        
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for i in range(n+2)] for j in range(n+2)]
        
        for i in range(n,0,-1):
            for j in range(1,n+1):
                if i > j:
                    continue
                ans = -math.inf
                for x in range(i,j+1):
                    cost = nums[i-1]*nums[x]*nums[j+1] +  dp[i][x-1] + dp[x+1][j]
                    ans = max(cost,ans)
                    
                dp[i][j] = ans               
                
        return dp[1][n]
    
                
                
            
        