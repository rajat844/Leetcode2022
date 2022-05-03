class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        end = -1
        mx = nums[0]
        
        for i in range(n):
            if nums[i] >= mx:
                mx = nums[i]
            else :
                end = i
        start = 0
        mn = nums[-1]
        
        for i in range(n-1,-1,-1):
            if nums[i] <= mn:
                mn = nums[i]
            else :
                start = i
        return end - start + 1
        