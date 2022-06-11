class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        p = 1
        ans = 0
        j = 0
        
        for i in range(len(nums)):
            p *= nums[i]
            
            while p >= k and j <= i:
                p = p//nums[j]
                j += 1
            
            ans += i-j+1
        
        return ans
            
        