class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        s = 0
        ans = 0
        
        j = 0
        
        for i in range(len(nums)):
            s += nums[i]
            while s* (i-j+1) >= k:
                s -= nums[j]
                j += 1
            ans += i-j+1
        
        return ans