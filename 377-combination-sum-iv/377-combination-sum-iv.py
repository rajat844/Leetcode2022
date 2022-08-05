class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def recursion(s):
            if s > target:
                return 0
            
            if s == target:
                return 1
            if dp[s] != None:
                return dp[s]
            
            temp = 0
            for x in range(len(nums)):
                temp += recursion(s+nums[x])
            
            dp[s] = temp
            return temp
                
                
        dp = [None for i in range(target+1)]
        return recursion(0)
        
        
                
        