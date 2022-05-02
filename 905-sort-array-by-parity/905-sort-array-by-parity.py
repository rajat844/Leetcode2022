class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        st = -1
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                st += 1
                nums[st],nums[i] = nums[i],nums[st]
                
        return nums
         
        