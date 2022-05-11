import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mn = 1
        mx = 1
        ans = max(nums)
        
        for i in range(len(nums)):
            if nums[i] == 0:
                mn = 1
                mx = 1
                continue
            else:
                currMin = min(mn * nums[i], mx * nums[i],nums[i])
                currMax = max(mn * nums[i], mx * nums[i],nums[i])
                
                ans = max(currMax,currMin,ans)
                mn,mx = currMin,currMax
                
        return ans