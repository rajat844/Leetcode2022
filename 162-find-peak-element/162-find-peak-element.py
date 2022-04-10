class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l = 0
        h = len(nums) - 1
        
        while l < h - 1:
            mid = (l + h) >> 1
            
            if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
                return mid
            elif nums[mid] < nums[mid+1]:
                l = mid + 1
            else :
                h = mid - 1
        
        return l if nums[l] >= nums[h] else h