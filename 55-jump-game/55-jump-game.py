class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [None for i in range(n)]
        dp[n-1] = True
        
        for i in range(n-2,-1,-1):
            x = nums[i]
            for j in range(i,i+x+1):
                if dp[j] == True:
                    dp[i] = True
                    break
        return dp[0]

                
                
        