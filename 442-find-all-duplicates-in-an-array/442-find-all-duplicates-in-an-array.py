class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ele = abs(nums[i])
            if nums[ele - 1] > 0:
                nums[ele-1] *= -1
            else:
                ans.append(ele)
        
        return ans