class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        st = 0
        
        for i in range(1,len(nums)):
            if nums[i] != nums[st]:
                st += 1
                nums[st] = nums[i]
        
        return st +1