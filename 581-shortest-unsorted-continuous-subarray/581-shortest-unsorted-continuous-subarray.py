class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        end = -1
        mx = nums[0]
        
        for i in range(1,len(nums)):
            if mx > nums[i]:
                end = i
            else :
                mx = nums[i]
        
        start = 0
        mn = nums[-1]
        
        for i in range(len(nums) - 2, -1, -1):
            if mn < nums[i]:
                start = i
            else :
                mn = nums[i]
        
        ans = end - start + 1
        return ans
        