class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        prevsum = 0
        
        for i in range(len(nums)):
            s -= nums[i]
            if s == prevsum:
                return i
            prevsum += nums[i]
        
        return -1
        