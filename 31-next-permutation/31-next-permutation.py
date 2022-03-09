class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = -1
        second = -1
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                first = i
                break
                
        if first == -1:
            return nums.reverse()
        
        else:
            for i in range(len(nums)-1,i,-1):
                if nums[i] > nums[first]:
                    second = i
                    break
            
            nums[first],nums[second] = nums[second],nums[first]
            
            nums[first+1:] = nums[first+1:][::-1]
        
        return nums
            