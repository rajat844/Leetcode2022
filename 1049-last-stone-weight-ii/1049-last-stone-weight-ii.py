class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #minimize the difference in subarrays
        target = sum(stones)
        
        dp = [[False for i in range(target+1)]for j in range(len(stones)+1)]
        
        for i in range(len(stones) + 1):
            dp[i][0] = True
            
            
        for i in range(1,len(stones)+1):
            for j in range(1,target + 1):
                if j >= stones[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-stones[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
         
        
        for i in range(target//2,-1,-1):
            if dp[-1][i] == True:
                return target - 2*i
            
            
                    
        
        
        
        