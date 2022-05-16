class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = len(nums)
        i = 0
        
        while i < end:
            if nums[i] == val:
                end -= 1
                nums[i],nums[end] = nums[end],nums[i]
            else :
                i += 1
                
        return i
                