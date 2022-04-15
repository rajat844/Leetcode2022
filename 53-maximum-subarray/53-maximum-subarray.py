import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -math.inf
        tillnow  = 0
        for i in range(len(nums)):
            if tillnow < 0:
                tillnow = nums[i]
            else :
                tillnow += nums[i]
            
            ans = max(ans,tillnow)
        
        return ans
        