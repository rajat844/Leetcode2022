class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(len(nums)):
            ans ^= nums[i]
            ans ^= i
        
        ans ^= len(nums)
        return ans
            