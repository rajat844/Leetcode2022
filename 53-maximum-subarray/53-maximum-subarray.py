import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        finalsum = -math.inf
        sumtillnow = 0
        
        for i in range(len(nums)):
            if sumtillnow > 0:
                sumtillnow += nums[i]
            
            else :
                sumtillnow = nums[i]
            
            finalsum = max(finalsum,sumtillnow)
        
        return finalsum
        
        
        