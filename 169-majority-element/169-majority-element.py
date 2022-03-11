class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ele = 0
        
        for i in range(len(nums)):
            if count == 0:
                ele = nums[i]
                count += 1
            elif ele == nums[i]:
                count += 1
            else :
                count -= 1
        
        if count > 0:
            return ele
        else :
            return -1