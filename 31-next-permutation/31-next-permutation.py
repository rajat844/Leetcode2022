class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) -1 
        n = len(nums)
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1
            
        if i == 0:
            nums.reverse()
            
        else :
            i = i-1
            
            while j > i:
                if nums[j] > nums[i]:
                    break
                j -= 1
            
            nums[i],nums[j] = nums[j],nums[i]
            
            nums[i+1:] = sorted(nums[i+1:])
            
        return nums