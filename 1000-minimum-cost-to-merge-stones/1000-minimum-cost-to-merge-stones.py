class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        if (n-1) % (K-1):
            return -1
        
        prefixSum = [0 for i in range(n+1)]
        
        for  i in range(1,n+1):
            prefixSum[i] = prefixSum[i-1] + stones[i-1]
        
        dp = [[[None for x in range(K+1)] for i in range(n+1)] for j in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                for k in range(1,K+1):
                    dp[i][j][k] = math.inf
                    
        
        for i in range(1,n+1):
            dp[i][i][1] = 0
        
        for l in range(2,n+1):
            for i in range(1,n-l+2):
                j = i+l-1
                for k in range(2,k+1):
                    for t in range(i,j):
                        dp[i][j][k] = min(dp[i][j][k],dp[i][t][k-1] + dp[t+1][j][1])
                
                dp[i][j][1] = dp[i][j][k] + prefixSum[j] - prefixSum[i-1]
                
        return dp[1][n][1]

        
        
        
            
                
            
            
        