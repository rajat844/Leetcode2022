class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        
        while l < h - 1:
            mid = (l + h) >> 1
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                h = mid - 1
        
        return l if nums[l]>= nums[h] else h
        