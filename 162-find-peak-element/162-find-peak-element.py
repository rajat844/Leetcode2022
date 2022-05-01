class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        i = 0
        j = n-1
        
        while i < j-1:
            mid = (i+j) >> 1
            if nums[mid - 1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid + 1] > nums[mid]:
                i = mid + 1
            else:
                j = mid - 1
        
        return i if nums[i] >= nums[j] else j
        