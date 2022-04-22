class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = -1
        second = -1
        
        i = len(nums) - 2
        
        while i >= 0 :
            if nums[i] < nums[i+1]:
                first = i
                break
            i -= 1
                
        if first == -1:
            nums = nums.reverse()
        
        else:
            
            for i in range(len(nums)-1,first,-1):
                if nums[i] > nums[first]:
                    second = i
                    break
            
            nums[first],nums[second] = nums[second],nums[first]
            
            nums[first + 1:] = nums[first+1:][::-1]
        