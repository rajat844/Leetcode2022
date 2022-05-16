class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        st = -1
        
        for curr in range(len(nums)):
            if nums[curr] != 0:
                st += 1
                nums[st] = nums[curr]
        
        for i in range(st+1,len(nums)):
            nums[i] = 0
        
                